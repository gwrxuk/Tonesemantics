import os
import json
import glob
from music21 import converter
from src.harmonic_analysis import HarmonicAnalyzer

def run_analysis():
    data_dir = "data"
    result_dir = "result"
    analysis_dir = "analysis"
    
    # Get all MIDI files
    midi_files = glob.glob(os.path.join(data_dir, "*.mid"))
    midi_files.sort()
    
    if not midi_files:
        print("No MIDI files found in data/")
        return

    summary_report = []

    for file_path in midi_files:
        filename = os.path.basename(file_path)
        base_name = os.path.splitext(filename)[0]
        print(f"Analyzing {filename}...")
        
        try:
            # Load Score
            score = converter.parse(file_path)
            
            # 1. Identify Key
            key_obj = HarmonicAnalyzer.identify_key(score)
            
            # 2. Roman Numeral Analysis
            # Note: harmonic_analysis.py returns (key, rn_sequence)
            _, rn_sequence = HarmonicAnalyzer.roman_numeral_analysis(score)
            
            # Prepare Result Data
            result_data = {
                "filename": filename,
                "detected_key": f"{key_obj.tonic.name} {key_obj.mode}",
                "confidence": key_obj.correlationCoefficient,
                "chord_count": len(rn_sequence),
                "roman_numerals": rn_sequence
            }
            
            # Save to result/ (JSON)
            json_path = os.path.join(result_dir, f"{base_name}_result.json")
            with open(json_path, 'w') as f:
                json.dump(result_data, f, indent=4)
            
            # Prepare Analysis Report Entry
            analysis_text = f"File: {filename}\n"
            analysis_text += f"Key: {result_data['detected_key']}\n"
            analysis_text += f"Progression: {' -> '.join(rn_sequence)}\n"
            analysis_text += "-" * 40 + "\n"
            
            summary_report.append(analysis_text)
            
            # Save individual analysis text
            txt_path = os.path.join(analysis_dir, f"{base_name}_analysis.txt")
            with open(txt_path, 'w') as f:
                f.write(analysis_text)
                
        except Exception as e:
            print(f"Error analyzing {filename}: {e}")

    # Save full summary
    with open(os.path.join(analysis_dir, "full_report.txt"), "w") as f:
        f.writelines(summary_report)
        
    print("Batch analysis complete.")

if __name__ == "__main__":
    run_analysis()

