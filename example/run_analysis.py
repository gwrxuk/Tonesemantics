import os
import sys
import matplotlib.pyplot as plt
import librosa.display
import numpy as np

# Ensure src is in python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.audio_analysis import AudioAnalyzer

def main():
    # Configuration
    input_file = os.path.join(os.path.dirname(__file__), "..", "music", "Mon morceau.m4a")
    output_dir = os.path.join(os.path.dirname(__file__))
    json_output_path = os.path.join(output_dir, "analysis_results.json")
    plot_output_path = os.path.join(output_dir, "analysis_plot.png")

    print(f"Processing file: {input_file}")
    
    if not os.path.exists(input_file):
        print(f"Error: Input file not found at {input_file}")
        return

    # Initialize Analyzer
    analyzer = AudioAnalyzer()
    
    # Run Analysis
    print("Running harmonic and rhythmic analysis...")
    results = analyzer.analyze_file(input_file)
    
    if "error" in results:
        print(results["error"])
        return

    # Save JSON results
    print(f"Saving JSON results to {json_output_path}")
    analyzer.save_analysis(results, json_output_path)
    
    # Generate Visualizations
    print("Generating visualizations...")
    try:
        y, sr = librosa.load(input_file, sr=22050)
        chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
        
        plt.figure(figsize=(10, 8))
        
        # Subplot 1: Waveform
        plt.subplot(2, 1, 1)
        librosa.display.waveshow(y, sr=sr)
        plt.title('Waveform')
        
        # Subplot 2: Chromagram
        plt.subplot(2, 1, 2)
        librosa.display.specshow(chroma, y_axis='chroma', x_axis='time')
        plt.colorbar()
        plt.title('Chromagram (Harmonic Content)')
        
        plt.tight_layout()
        plt.savefig(plot_output_path)
        print(f"Plot saved to {plot_output_path}")
        
    except Exception as e:
        print(f"Error generating plot: {e}")

    print("Analysis complete.")

if __name__ == "__main__":
    main()

