
from file_type_checker import FileTypeChecker  
from whisper_transcriber import Transcriber
from file_save_txt import TextSaver
import torch
import os

AUDIO_DIR = 'Notetaker.ai_v1/data/audio_inputs/To_be_transcribed' 
CACHE_DIR = 'Notetaker.ai_v1/data/cache/wav'
TRANSCRIBED_DIR = 'Notetaker.ai_v1/data/audio_inputs/Transcribed'

class Notetaker:
    def __init__(self, audio_dir, cache_dir):
        self.audio_dir = audio_dir
        self.cache_dir = cache_dir

    def transcribe_audio_files(self):
        checker = FileTypeChecker(self.audio_dir, self.cache_dir)
        checker.convert_files()

        # Loop through converted WAV files in CACHE_DIR and transcribe each file
        for filename in os.listdir(self.cache_dir):
            if filename.endswith(".wav"):
                audio_file_path = os.path.join(self.cache_dir, filename)
                transcriber = Transcriber(audio_file_path=audio_file_path)
                result = transcriber.transcribe()
                print(f"Transcription for {filename}:")
                print(result["text"])

                # Saving the transcription result to a .txt file using TextSaver
                base_name = os.path.splitext(filename)[0]  # Removing the .wav extension
                saver = TextSaver(content=result["text"], loaded_file_name=base_name)
                saver.save()

        # Clear the cache directory
        self.clear_cache()

        # Move the transcribed files to the designated directory
        self.move_transcribed_files()

        # Cleanup resources
        transcriber.close()
        torch.cuda.empty_cache()
        print("Resources released and GPU cache emptied.")

    def clear_cache(self):
        print("Clearing cache directory...")
        for filename in os.listdir(self.cache_dir):
            file_path = os.path.join(self.cache_dir, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    os.rmdir(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")

    def move_transcribed_files(self):
        print("Moving transcribed files...")
        if not os.path.exists(TRANSCRIBED_DIR):
            os.makedirs(TRANSCRIBED_DIR)
        for filename in os.listdir(self.audio_dir):
            source_path = os.path.join(self.audio_dir, filename)
            target_path = os.path.join(TRANSCRIBED_DIR, filename)
            os.rename(source_path, target_path)

if __name__ == "__main__":
    notetaker = Notetaker(AUDIO_DIR, CACHE_DIR)
    notetaker.transcribe_audio_files()
