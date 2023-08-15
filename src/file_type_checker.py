import os
from pydub import AudioSegment
import shutil

SUPPORTED_FORMATS = ['mp4', 'mp3', 'ogg', 'flv', 'm4a', 'wma']  # Top-level constant

class FileTypeChecker:

    def __init__(self, audio_dir, cache_dir):
        print("Initializing FileTypeChecker...")
        self.audio_dir = audio_dir
        self.cache_dir = cache_dir

    def convert_files(self):
        print(f"Creating cache directory at {self.cache_dir}...")
        os.makedirs(self.cache_dir, exist_ok=True)
        print("Cache directory ready.")

        print(f"Scanning directory {self.audio_dir} for audio files...")
        for filename in os.listdir(self.audio_dir):
            print(f"Processing file: {filename}")
            self._process_file(filename)

    def _process_file(self, filename):  # Seperate method to reduce nesting
        filepath = os.path.join(self.audio_dir, filename)
        base, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lstrip(".").lower()

        if file_extension == 'wav':
            print(f"Copying WAV file {filename} to cache directory...")
            shutil.copy(filepath, os.path.join(self.cache_dir, filename))
            return  # Skip further processing for WAV files
        
        if file_extension not in SUPPORTED_FORMATS:
            print(f"Skipping unsupported format: {file_extension}")
            return  # Skip unsupported formats

        try:
            print(f"Converting {filename} to WAV format...")
            audio_segment = AudioSegment.from_file(filepath, format=file_extension)
            wav_path = os.path.join(self.cache_dir, base + '.wav')
            audio_segment.export(wav_path, format='wav')
            print(f"Conversion successful for {filename}. Saved as {base}.wav")
        except Exception as e:
            print(f"Error processing {filename}: {e}")