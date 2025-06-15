#!/usr/bin/env python3
"""
Audio Streaming Backend Application

This script manages an MP3 audio streaming service with the following features:
- SQLite database for storing MP3 files and play history
- Randomized playlist generation
- Prevention of repeating the same song within 24 hours
- Streaming via ffmpeg to an RTMP endpoint
"""

import os
import sys
import time
import random
import sqlite3
import datetime
import subprocess
import logging
import signal
import atexit
from pathlib import Path
from typing import List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger('audio-streaming')

# Configuration
DEFAULT_AUDIO_DIR = "/var/www/html/mcradio/public/audios"
DEFAULT_DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "audio_library.db")
RTMP_ENDPOINT = "rtmp://localhost/radio/stream"
STREAM_BITRATE = "128000"
STREAM_SAMPLE_RATE = "44100"
STREAM_TITLE = "MedinaCheikh Radio"


class AudioDatabase:
    """Manages the SQLite database for audio files and play history."""

    def __init__(self, db_path: str = DEFAULT_DB_PATH):
        """Initialize the database connection and create tables if they don't exist."""
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.create_tables()

    def create_tables(self):
        """Create the necessary database tables if they don't exist."""
        cursor = self.conn.cursor()

        # Table for audio files
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS audio_files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT UNIQUE NOT NULL,
            path TEXT NOT NULL,
            added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')

        # Table for play history
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS play_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            audio_id INTEGER NOT NULL,
            played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (audio_id) REFERENCES audio_files (id)
        )
        ''')

        self.conn.commit()

    def add_audio_file(self, filename: str, path: str) -> int:
        """Add an audio file to the database if it doesn't exist."""
        cursor = self.conn.cursor()
        try:
            print(f"Adding audio file ${filename}")

            cursor.execute(
                "INSERT OR IGNORE INTO audio_files (filename, path) VALUES (?, ?)",
                (filename, path)
            )
            self.conn.commit()

            # Get the ID of the inserted or existing record
            cursor.execute("SELECT id FROM audio_files WHERE filename = ?", (filename,))
            result = cursor.fetchone()
            return result['id'] if result else None
        except sqlite3.Error as e:
            logger.error(f"Database error adding audio file: {e}")
            return None

    def record_play(self, audio_id: int):
        """Record that an audio file was played."""
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO play_history (audio_id) VALUES (?)",
                (audio_id,)
            )
            self.conn.commit()
        except sqlite3.Error as e:
            logger.error(f"Database error recording play: {e}")

    def get_all_audio_files(self) -> List[dict]:
        """Get all audio files from the database."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM audio_files")
        return [dict(row) for row in cursor.fetchall()]

    def get_recently_played(self, hours: int = 36) -> List[int]:
        """Get IDs of audio files played within the specified x hours."""
        cursor = self.conn.cursor()
        time_threshold = datetime.datetime.now() - datetime.timedelta(hours=hours)
        cursor.execute(
            "SELECT DISTINCT audio_id FROM play_history WHERE played_at > ?",
            (time_threshold.strftime('%Y-%m-%d %H:%M:%S'),)
        )
        return [row['audio_id'] for row in cursor.fetchall()]

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()


class AudioStreamer:
    """Manages the audio streaming process."""

    def __init__(self, audio_dir: str = DEFAULT_AUDIO_DIR, db_path: str = DEFAULT_DB_PATH):
        """Initialize the audio streamer with the specified directory and database."""
        self.audio_dir = audio_dir
        self.db = AudioDatabase(db_path)
        self.current_process = None

    def scan_audio_files(self):
        """Scan the audio directory for MP3 files and update the database."""
        logger.info(f"Scanning for MP3 files in {self.audio_dir}")
        try:
            audio_files = list(Path(self.audio_dir).glob("*.mp3"))
            for audio_file in audio_files:
                self.db.add_audio_file(audio_file.name, str(audio_file))
            logger.info(f"Found {len(audio_files)} MP3 files")
        except Exception as e:
            logger.error(f"Error scanning audio files: {e}")

    def create_playlist(self) -> List[dict]:
        """Create a randomized playlist avoiding recently played files."""
        all_files = self.db.get_all_audio_files()
        if not all_files:
            logger.warning("No audio files found in database")
            return []

        # Get IDs of recently played files
        recently_played_ids = set(self.db.get_recently_played())

        # Filter out recently played files if possible
        available_files = [f for f in all_files if f['id'] not in recently_played_ids]

        # If all files were recently played, use all files
        if not available_files:
            logger.info("All files were recently played, using complete library")
            available_files = all_files

        # Shuffle the available files
        random.shuffle(available_files)

        return available_files

    def create_ffmpeg_playlist(self, playlist: List[dict]) -> str:
        """Create a temporary playlist file for FFmpeg."""
        playlist_path = os.path.join(self.audio_dir, "ffmpeg_playlist.txt")
        with open(playlist_path, 'w') as f:
            for audio in playlist:
                f.write(f"file '{audio['path']}'\n")

        print(f"Playlist file '{playlist_path}' created")
        return playlist_path

    def stream_audio(self, playlist_path: str):
        """Stream audio using FFmpeg to the RTMP endpoint."""
        cmd = [
            "ffmpeg",
            "-re",
            "-f", "concat",
            "-safe", "0",
            "-i", playlist_path,
            "-metadata", f"title={STREAM_TITLE}",
            "-ab", STREAM_BITRATE,
            "-ar", STREAM_SAMPLE_RATE,
            "-vn",
            "-c:a", "aac",
            "-f", "flv",
            RTMP_ENDPOINT
        ]

        logger.info(f"Starting FFmpeg streaming process")
        try:
            # Close any existing process first
            if self.current_process is not None:
                self._terminate_process()

            # Start new process
            self.current_process = subprocess.Popen(
                cmd, 
                stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )
            return self.current_process
        except Exception as e:
            logger.error(f"Error starting FFmpeg: {e}")
            self.current_process = None
            return None

    def run(self):
        """Run the audio streaming service continuously."""
        logger.info("Starting audio streaming service")

        while True:
            try:
                # Scan for audio files
                self.scan_audio_files()

                # Create a randomized playlist
                playlist = self.create_playlist()
                if not playlist:
                    logger.error("Failed to create playlist, no audio files available")
                    time.sleep(10)
                    continue

                # Create FFmpeg playlist file
                playlist_path = self.create_ffmpeg_playlist(playlist)

                # Log the playlist
                logger.info("Created playlist with the following files:")
                for i, audio in enumerate(playlist, 1):
                    logger.info(f"{i}. {audio['filename']}")

                # Start streaming
                print("Starting audio streaming...")
                process = self.stream_audio(playlist_path)
                if not process:
                    logger.error("Failed to start streaming process")
                    time.sleep(10)
                    continue

                # Record plays as they happen
                for audio in playlist:
                    # Wait for the current file to start playing
                    # This is a simplification - in a real app, you'd parse FFmpeg output
                    # to determine when each file starts playing
                    logger.info(f"Now playing: {audio['filename']}")
                    self.db.record_play(audio['id'])
                    time.sleep(5)  # Just a placeholder, not accurate

                # Wait for the process to complete with a timeout
                try:
                    # Check if process is still running
                    if process.poll() is None:
                        # Process is still running, wait for it with a timeout
                        # This prevents indefinite blocking if the process hangs
                        exit_code = process.wait(timeout=3600)  # 1 hour timeout
                        logger.info(f"Streaming process completed with exit code {exit_code}, restarting...")
                    else:
                        # Process already completed
                        logger.info(f"Streaming process already completed with exit code {process.returncode}, restarting...")
                except subprocess.TimeoutExpired:
                    # Process is taking too long, terminate it and restart
                    logger.warning("Streaming process timeout expired, terminating and restarting...")
                    self._terminate_process()

            except KeyboardInterrupt:
                logger.info("Received interrupt, shutting down...")
                break
            except Exception as e:
                logger.error(f"Error in streaming loop: {e}")
                # Make sure to terminate any running process before continuing
                self._terminate_process()
                time.sleep(10)

    def _terminate_process(self):
        """Terminate the current FFmpeg process if it exists."""
        if self.current_process is not None:
            logger.info("Terminating existing FFmpeg process")
            try:
                # Check if process is still running
                if self.current_process.poll() is None:
                    # Process is still running, terminate it
                    self.current_process.terminate()
                    # Give it a moment to terminate gracefully
                    try:
                        self.current_process.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        # Force kill if it doesn't terminate gracefully
                        logger.warning("FFmpeg process did not terminate gracefully, forcing kill")
                        self.current_process.kill()
                        self.current_process.wait()
            except Exception as e:
                logger.error(f"Error terminating FFmpeg process: {e}")
            finally:
                # Close file descriptors
                if hasattr(self.current_process, 'stdout') and self.current_process.stdout:
                    self.current_process.stdout.close()
                if hasattr(self.current_process, 'stderr') and self.current_process.stderr:
                    self.current_process.stderr.close()
                self.current_process = None

    def cleanup(self):
        """Clean up resources."""
        self._terminate_process()
        self.db.close()


def main():
    """Main entry point for the application."""
    import argparse

    parser = argparse.ArgumentParser(description="Audio Streaming Backend")
    parser.add_argument(
        "--audio-dir", 
        default=DEFAULT_AUDIO_DIR,
        help=f"Directory containing MP3 files (default: {DEFAULT_AUDIO_DIR})"
    )
    parser.add_argument(
        "--db-path", 
        default=DEFAULT_DB_PATH,
        help=f"Path to SQLite database file (default: {DEFAULT_DB_PATH})"
    )

    args = parser.parse_args()

    streamer = AudioStreamer(args.audio_dir, args.db_path)

    # Flag to track if cleanup has been done
    cleanup_done = False

    # Register cleanup handlers
    def cleanup_handler(signum=None, frame=None):
        nonlocal cleanup_done
        if not cleanup_done:
            logger.info(f"Received signal {signum if signum else 'EXIT'}, cleaning up...")
            streamer.cleanup()
            cleanup_done = True
        sys.exit(0)

    # Register signal handlers
    signal.signal(signal.SIGTERM, cleanup_handler)
    signal.signal(signal.SIGINT, cleanup_handler)

    # Register atexit handler
    atexit.register(lambda: cleanup_handler() if not cleanup_done else None)

    try:
        streamer.run()
    except KeyboardInterrupt:
        logger.info("Shutting down...")
    finally:
        if not cleanup_done:
            streamer.cleanup()
            cleanup_done = True


if __name__ == "__main__":
    main()
