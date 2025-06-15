# Audio Streaming Backend

A Python backend application for streaming MP3 audio files using FFmpeg. This application replaces the original `stream-audio.bash` script with a more robust solution that includes database tracking of audio files and play history.

## Features

- SQLite database for storing MP3 files and play history
- Randomized playlist generation
- Prevention of repeating the same song within 24 hours
- Streaming via FFmpeg to an RTMP endpoint
- Detailed logging of streaming activity

## Requirements

- Python 3.6+
- FFmpeg installed and available in PATH
- SQLite3 (included in Python standard library)

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd audio-streaming
   ```

2. (Optional) Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies (if any):
   ```
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

Run the application with default settings:

```
python main.py
```

This will:
1. Scan the default audio directory (`/var/www/html/mcradio/public/audios`)
2. Create a SQLite database in the application directory
3. Generate a randomized playlist
4. Stream audio to the default RTMP endpoint (`rtmp://localhost/radio/stream`)

### Command Line Options

The application supports the following command line options:

- `--audio-dir`: Directory containing MP3 files
  ```
  python main.py --audio-dir /path/to/mp3/files
  ```

- `--db-path`: Path to SQLite database file
  ```
  python main.py --db-path /path/to/database.db
  ```

### Example

```
python main.py --audio-dir /home/user/music --db-path /var/lib/audio-streaming/library.db
```

## Testing

Run the test suite to verify the application's functionality:

```
python test_audio_streamer.py
```

## How It Works

1. **Database Management**: The application uses SQLite to store information about audio files and when they were last played.

2. **File Scanning**: On startup, the application scans the specified directory for MP3 files and adds them to the database.

3. **Playlist Generation**: A randomized playlist is created, prioritizing files that haven't been played in the last 24 hours.

4. **Streaming**: FFmpeg is used to stream the audio files to the specified RTMP endpoint.

5. **Play History**: As each file is played, its play time is recorded in the database to ensure it's not repeated too soon.

6. **Process Management**: The application implements robust subprocess management for FFmpeg:
   - Proper process termination and cleanup to prevent defunct processes
   - Signal handling to ensure clean shutdown on SIGTERM and SIGINT
   - Timeout-based process monitoring to prevent hanging
   - Resource cleanup to avoid file descriptor leaks

## Configuration

Default configuration values are set at the top of `main.py`:

- `DEFAULT_AUDIO_DIR`: Directory containing MP3 files
- `DEFAULT_DB_PATH`: Path to SQLite database file
- `RTMP_ENDPOINT`: RTMP streaming endpoint
- `STREAM_BITRATE`: Audio bitrate for streaming
- `STREAM_SAMPLE_RATE`: Audio sample rate for streaming
- `STREAM_TITLE`: Metadata title for the stream

## License

[MIT License](LICENSE)
