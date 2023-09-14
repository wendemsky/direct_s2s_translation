import os


def rename_mp3_files(folder_path):
    files = os.listdir(folder_path)
    mp3_files = [f for f in files if f.lower().endswith('.mp3')]

    print(f'Folder path: {folder_path}')
    print(f'All files in the folder: {files}')
    print(f'MP3 files found: {len(mp3_files)}')

    for index, mp3_file in enumerate(mp3_files, start=1):
        old_path = os.path.join(folder_path, mp3_file)
        new_path = os.path.join(folder_path, f'{index}.mp3')
        os.rename(old_path, new_path)
        print(f'Renamed {old_path} to {new_path}')


if __name__ == "__main__":
    folder_path_en = r'/content/english_audio'  # Change this to your mp3 file folder
    folder_path_kr = r'/content/korean_audio'
    rename_mp3_files(folder_path_en)
    rename_mp3_files(folder_path_kr)
    print("MP3 files renamed successfully!")
