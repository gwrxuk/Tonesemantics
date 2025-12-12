import os
from typing import List, Optional, Union
import music21
import pretty_midi

class MusicDataLoader:
    """
    Handles loading and basic preprocessing of symbolic music data (MusicXML, MIDI).
    """
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir

    def load_midi(self, file_path: str) -> Optional[pretty_midi.PrettyMIDI]:
        """Loads a MIDI file."""
        try:
            pm = pretty_midi.PrettyMIDI(file_path)
            return pm
        except Exception as e:
            print(f"Error loading MIDI file {file_path}: {e}")
            return None

    def load_musicxml(self, file_path: str) -> Optional[music21.stream.Score]:
        """Loads a MusicXML file."""
        try:
            score = music21.converter.parse(file_path)
            return score
        except Exception as e:
            print(f"Error loading MusicXML file {file_path}: {e}")
            return None

    def get_files_by_extension(self, extension: str) -> List[str]:
        """Recursively finds files with a specific extension in data_dir."""
        files = []
        for root, _, filenames in os.walk(self.data_dir):
            for filename in filenames:
                if filename.lower().endswith(extension.lower()):
                    files.append(os.path.join(root, filename))
        return files

if __name__ == "__main__":
    # Example usage
    loader = MusicDataLoader()
    print("MusicDataLoader initialized.")

