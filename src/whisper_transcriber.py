from whisper import transcribe, load_model, load_audio
import torch

class Transcriber:
    def __init__(self, audio_file_path, device_type="small"):
        print("Initializing Transcriber...")
        self.device_type = device_type
        self.audio_file_path = audio_file_path
        print(f"Set audio file path: {self.audio_file_path}")
        
        self.device = self.get_device()
        print(f"Using device: {self.device}")
        
        with torch.cuda.device(self.device):
            self.model = self.load_model()
        print("Model loaded successfully.")
        
        self.args = self.construct_args()
        print("Arguments constructed.")

    def get_device(self):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        return device

    def load_model(self):
        return load_model(self.device_type, device=self.device)

    def get_args(self):
        return self.args

    def construct_args(self):
        args = {
            "model": self.model,
            "audio": self.audio_file_path,
            "verbose": True,
            "temperature": 0.2,
            "compression_ratio_threshold": 2.4,
            "logprob_threshold": -1.0,
            "no_speech_threshold": 0.6,
            "condition_on_previous_text": True,
            "word_timestamps": False,
            "prepend_punctuations": "'“¿([{-",
            "append_punctuations": "\"'.。,，!！?？:：”)]}、",
            "language": "en",
        }
        return args

    def transcribe(self):
        print(f"Transcribing audio from: {self.audio_file_path}")
        return transcribe(**self.args)
    def close(self):
        self.model.to('cpu')
        del self.model
        print("Transcriber resources released.")
