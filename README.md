Here is a draft README.md for the Notetaker program:

# Notetaker

Notetaker is a program that can transcribe audio files in various formats to text using Whisper. It converts input audio files to WAV format, splits long files into chunks, transcribes each chunk using Whisper, and saves the output as a text file.

## Files

- `main.py` - The main driver program. Creates instance of Notetaker and calls transcribe_audio_files()
- `notetaker.py` - Notetaker class that handles the transcription process.
- `file_type_checker.py` - Converts input audio files to WAV format.
- `whisper_transcriber.py` - Transcribes WAV files using Whisper. Splits long files.
- `file_save_txt.py` - Saves transcribed text to output .txt files.

## Usage

1. Place input audio files in `AUDIO_DIR` folder. Supported formats: mp3, m4a, wav, ogg, etc.

2. Run `python main.py`

3. Transcribed .txt files will be saved in `OUTPUT_DIR` folder.

4. Modify `AUDIO_DIR`, `CACHE_DIR`, `OUTPUT_DIR` as needed in code. 

## Customization

- To use a different Whisper model, modify `device_type` in `whisper_transcriber.py`
- To change maximum audio length, modify `MAX_LENGTH` in `whisper_transcriber.py`  
- To customize Whisper arguments, modify `construct_args()` in `whisper_transcriber.py`

## Requirements

- Python 3.7+ 
- Whisper
- Pydub
- Torch

Please let me know if you would like me to expand or modify the README further.