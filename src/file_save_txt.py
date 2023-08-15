import os
from datetime import datetime

class TextSaver:
    OUTPUT_DIR = "Notetaker.ai_v1/data/output/txt"  # Directory to save .txt files
    
    def __init__(self, content, loaded_file_name):
        """
        Initialize the TextSaver class.
        
        Args:
        - content (str): The transcribed text content to save.
        - loaded_file_name (str): The name of the loaded audio file.
        """
        self.content = content
        self.loaded_file_name = loaded_file_name

    def save(self):
        """
        Save the transcribed content to a .txt file in the specified directory.
        """
        # Ensure the output directory exists
        os.makedirs(TextSaver.OUTPUT_DIR, exist_ok=True)
        
        # Create default name for .txt files
        default_name = f"{self.loaded_file_name}_transcribed_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
        output_path = os.path.join(TextSaver.OUTPUT_DIR, default_name)
        
        try:
            with open(output_path, "w") as f:
                f.write(self.content)
            
            print(f"File saved at {output_path}")
        
        except Exception as e:
            print(f"Failed to save file: {e}")

# Example usage:
# text_content = "This is the transcribed text content."
# saver = TextSaver(content=text_content, loaded_file_name="sample_audio")
# saver.save()