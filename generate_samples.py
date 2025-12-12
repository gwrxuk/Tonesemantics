import os
from music21 import stream, key, note, chord, meter, instrument

def create_progression(name, k_str, progression_data):
    """
    progression_data: list of tuples (chord_notes_list, duration)
    """
    s = stream.Score()
    p = stream.Part()
    p.insert(0, instrument.Piano())
    k = key.Key(k_str)
    p.insert(0, k)
    p.insert(0, meter.TimeSignature('4/4'))

    for notes, dur in progression_data:
        # Create chord
        c = chord.Chord(notes)
        c.quarterLength = dur
        p.append(c)

    s.insert(0, p)
    
    filename = os.path.join("data", f"{name}.mid")
    s.write('midi', fp=filename)
    print(f"Created {filename}")

def main():
    if not os.path.exists("data"):
        os.makedirs("data")

    # 1. C Major: I - IV - V - I
    create_progression("sample_01_c_major", "C", [
        (['C4', 'E4', 'G4', 'C5'], 1.0), # I
        (['F4', 'A4', 'C5', 'F5'], 1.0), # IV
        (['G4', 'B4', 'D5', 'G5'], 1.0), # V
        (['C4', 'E4', 'G4', 'C5'], 4.0), # I
    ])

    # 2. A Minor: i - iv - V7 - i
    create_progression("sample_02_a_minor", "a", [
        (['A3', 'C4', 'E4', 'A4'], 1.0), # i
        (['D4', 'F4', 'A4', 'D5'], 1.0), # iv
        (['E4', 'G#4', 'B4', 'D5'], 1.0), # V7
        (['A3', 'C4', 'E4', 'A4'], 4.0), # i
    ])

    # 3. G Major: I - vi - ii - V - I
    create_progression("sample_03_g_major", "G", [
        (['G3', 'B3', 'D4', 'G4'], 1.0), # I
        (['E4', 'G4', 'B4', 'E5'], 1.0), # vi
        (['A3', 'C4', 'E4', 'A4'], 1.0), # ii
        (['D4', 'F#4', 'A4', 'D5'], 1.0), # V
        (['G3', 'B3', 'D4', 'G4'], 4.0), # I
    ])

    # 4. F Major: I - V6/5 - I - IV - I
    create_progression("sample_04_f_major", "F", [
        (['F3', 'A3', 'C4', 'F4'], 2.0), # I
        (['E3', 'G3', 'B-3', 'C4'], 2.0), # V6/5 (approx voicing)
        (['F3', 'A3', 'C4', 'F4'], 2.0), # I
        (['B-3', 'D4', 'F4', 'B-4'], 2.0), # IV
        (['F3', 'A3', 'C4', 'F4'], 4.0), # I
    ])

    # 5. D Minor: i - VI - ii° - V - i
    create_progression("sample_05_d_minor", "d", [
        (['D4', 'F4', 'A4', 'D5'], 1.0), # i
        (['B-3', 'D4', 'F4', 'B-4'], 1.0), # VI
        (['E4', 'G4', 'B-4', 'E5'], 1.0), # ii dim
        (['A3', 'C#4', 'E4', 'A4'], 1.0), # V
        (['D4', 'F4', 'A4', 'D5'], 4.0), # i
    ])

if __name__ == "__main__":
    main()

