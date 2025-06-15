import os
import time
import random

# McRadio RTMP Streaming
# Add new medias to shuffled_audios file

def get_media(path):
    """Get a list of MP3 files in the specified folder."""
    media = [f for f in os.listdir(path) if f.endswith('.mp3')]
    return media

def insert_media(files_list, new_media):
    """Randomly insert new media files into the existing list."""
    # Check if today's date matches the file's last modification date
    yester_timestamp = time.time() - (24 * 60 * 60)

    today_files = [f for f in new_media if os.path.getmtime(f) > yester_timestamp]
    print(f"{len(today_files)} new files detected : \n", today_files)

    # Insert new media files randomly into the existing list, from the middle
    middle = len(files_list) // 2
    
    for f in today_files:
        ridx = random.randint(middle, len(files_list))
        print(f"Inserting {f} at index {ridx}")
        files_list[ridx:ridx] = [f]
    print(f"New total count {len(files_list)}")

def main():
    playlist = 'shuffled_audios'
    audios_path = './'

    # Read existing MP3 files from the text file
    with open(playlist, 'r') as file:
        media_files = [line.strip() for line in file]
        print("Existing media files count: ", len(media_files))

    # Get a list of new media files in the specified folder
    new_media_src = get_media(audios_path)

    # Insert new media files into the existing list
    insert_media(media_files, new_media_src)

    # Write the updated list back to the text file
    with open(playlist, 'w') as file:
        file.write('\n'.join(media_files))


if __name__ == "__main__":
    main()
