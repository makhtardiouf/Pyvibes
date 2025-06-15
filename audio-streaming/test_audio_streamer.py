#!/usr/bin/env python3
"""
Test script for the audio streaming backend application.
This script tests the core functionality without actually streaming.
"""

import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock

# Import from main.py
from main import AudioDatabase, AudioStreamer

class TestAudioDatabase(unittest.TestCase):
    """Test the AudioDatabase class."""
    
    def setUp(self):
        """Set up a temporary database for testing."""
        self.temp_db = tempfile.NamedTemporaryFile(suffix='.db').name
        self.db = AudioDatabase(self.temp_db)
    
    def tearDown(self):
        """Clean up after tests."""
        self.db.close()
        if os.path.exists(self.temp_db):
            os.remove(self.temp_db)
    
    def test_add_audio_file(self):
        """Test adding an audio file to the database."""
        audio_id = self.db.add_audio_file("test.mp3", "./test.mp3")
        self.assertIsNotNone(audio_id)
        
        # Check if the file was added
        files = self.db.get_all_audio_files()
        self.assertEqual(len(files), 1)
        self.assertEqual(files[0]['filename'], "test.mp3")
        self.assertEqual(files[0]['path'], "./test.mp3")
    
    def test_record_play(self):
        """Test recording a play in the history."""
        audio_id = self.db.add_audio_file("test.mp3", "./test.mp3")
        self.db.record_play(audio_id)
        
        # Check if the play was recorded
        recently_played = self.db.get_recently_played()
        self.assertEqual(len(recently_played), 1)
        self.assertEqual(recently_played[0], audio_id)
    
    def test_get_recently_played(self):
        """Test getting recently played files."""
        # Add some files
        audio_id1 = self.db.add_audio_file("test1.mp3", "./test1.mp3")
        audio_id2 = self.db.add_audio_file("test2.mp3", "./test2.mp3")
        audio_id3 = self.db.add_audio_file("test3.mp3", "./test3.mp3")
        
        # Record some plays
        self.db.record_play(audio_id1)
        self.db.record_play(audio_id2)
        
        # Check recently played
        recently_played = self.db.get_recently_played()
        self.assertEqual(len(recently_played), 2)
        self.assertIn(audio_id1, recently_played)
        self.assertIn(audio_id2, recently_played)
        self.assertNotIn(audio_id3, recently_played)


class TestAudioStreamer(unittest.TestCase):
    """Test the AudioStreamer class."""
    
    def setUp(self):
        """Set up a temporary directory and database for testing."""
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_db = tempfile.NamedTemporaryFile(suffix='.db').name
        
        # Create some dummy MP3 files
        for i in range(5):
            with open(os.path.join(self.temp_dir.name, f"test{i}.mp3"), 'w') as f:
                f.write("dummy content")
        
        self.streamer = AudioStreamer(self.temp_dir.name, self.temp_db)
    
    def tearDown(self):
        """Clean up after tests."""
        self.streamer.cleanup()
        self.temp_dir.cleanup()
        if os.path.exists(self.temp_db):
            os.remove(self.temp_db)
    
    def test_scan_audio_files(self):
        """Test scanning for audio files."""
        self.streamer.scan_audio_files()
        
        # Check if files were added to the database
        files = self.streamer.db.get_all_audio_files()
        self.assertEqual(len(files), 5)
    
    def test_create_playlist(self):
        """Test creating a randomized playlist."""
        # First scan for files
        self.streamer.scan_audio_files()
        
        # Create a playlist
        playlist = self.streamer.create_playlist()
        self.assertEqual(len(playlist), 5)
        
        # Record some plays
        for audio in playlist[:3]:
            self.streamer.db.record_play(audio['id'])
        
        # Create a new playlist - should prefer the 2 unplayed files
        new_playlist = self.streamer.create_playlist()
        self.assertEqual(len(new_playlist), 5)
        
        # Check if the first 2 files in the new playlist were not played before
        played_ids = [audio['id'] for audio in playlist[:3]]
        self.assertNotIn(new_playlist[0]['id'], played_ids)
        self.assertNotIn(new_playlist[1]['id'], played_ids)
    
    @patch('subprocess.Popen')
    def test_stream_audio(self, mock_popen):
        """Test streaming audio with FFmpeg."""
        # Mock the subprocess.Popen
        mock_process = MagicMock()
        mock_popen.return_value = mock_process
        
        # Create a temporary playlist file
        playlist_path = os.path.join(self.temp_dir.name, "test_playlist.txt")
        with open(playlist_path, 'w') as f:
            f.write("file 'test.mp3'\n")
        
        # Test streaming
        process = self.streamer.stream_audio(playlist_path)
        self.assertIsNotNone(process)
        mock_popen.assert_called_once()


if __name__ == "__main__":
    unittest.main()