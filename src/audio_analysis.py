import librosa
import numpy as np
import json
from typing import Dict, Any

class AudioAnalyzer:
    """
    Analyzer for audio files (wav, mp3, m4a, etc.) focusing on harmonic content.
    """
    
    def __init__(self, sample_rate: int = 22050):
        self.sr = sample_rate

    def analyze_file(self, file_path: str) -> Dict[str, Any]:
        """
        Loads an audio file and performs harmonic and rhythmic analysis.
        """
        try:
            # Load audio
            y, sr = librosa.load(file_path, sr=self.sr)
        except Exception as e:
            return {"error": f"Could not load audio file: {e}"}

        # Harmonic-Percussive Source Separation
        y_harmonic, y_percussive = librosa.effects.hpss(y)

        # 1. Tempo and Beat Tracking
        tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr)
        
        # 2. Chromagram (Harmonic content)
        chroma = librosa.feature.chroma_cqt(y=y_harmonic, sr=sr)
        
        # 3. Key Estimation (Simple heuristic using chroma mean)
        # Sum chroma over time to get a pitch class distribution
        chroma_mean = np.mean(chroma, axis=1)
        # This is a very basic heuristic; sophisticated key finding would use templates
        key_index = np.argmax(chroma_mean)
        pitch_classes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        estimated_key = pitch_classes[key_index]

        # 4. Tonnetz (Tonal centroid features)
        tonnetz = librosa.feature.tonnetz(y=y_harmonic, sr=sr)

        analysis_results = {
            "tempo": float(tempo),
            "estimated_key_root": estimated_key,
            "duration": float(librosa.get_duration(y=y, sr=sr)),
            "beat_frames_count": len(beat_frames),
            "chroma_mean": chroma_mean.tolist(),
            "tonnetz_mean": np.mean(tonnetz, axis=1).tolist()
        }
        
        return analysis_results

    def save_analysis(self, results: Dict[str, Any], output_path: str):
        """Saves analysis results to a JSON file."""
        with open(output_path, 'w') as f:
            json.dump(results, f, indent=4)

