import os
from music21 import stream, key, chord, meter, instrument, note, interval, pitch

def create_sample(name, parts_data, time_sig='4/4', key_sig=None):
    """
    parts_data: list of lists, where each inner list represents a part (voice) 
    and contains tuples of (note_name, duration).
    """
    s = stream.Score()
    
    if key_sig:
        k = key.Key(key_sig)
    else:
        k = key.Key('C') # Default

    for part_idx, part_notes in enumerate(parts_data):
        p = stream.Part()
        p.id = f'Part-{part_idx+1}'
        p.insert(0, instrument.Piano()) # Use piano for simplicity
        p.insert(0, k)
        p.insert(0, meter.TimeSignature(time_sig))
        
        for n_str, dur in part_notes:
            if n_str == 'r':
                n = note.Rest()
            else:
                n = note.Note(n_str)
            n.quarterLength = dur
            p.append(n)
        
        s.insert(0, p)
    
    filename = os.path.join("data", f"{name}.mid")
    s.write('midi', fp=filename)
    print(f"Created {filename}")

def main():
    if not os.path.exists("data"):
        os.makedirs("data")

    # 13th Century: Medieval / Organum Style (Parallel 5ths)
    # Cantus firmus in lower voice, parallel 5th above
    create_sample("century_13_medieval", [
        [('D4', 2), ('E4', 2), ('F4', 2), ('D4', 2)], # Vox Organalis (5th above) -> Modified to be simpler parallel
        [('G3', 2), ('A3', 2), ('B-3', 2), ('G3', 2)]  # Vox Principalis
    ], time_sig='2/4', key_sig='g') # G Dorian approx

    # 14th Century: Ars Nova (Landini Cadence approx - 7-6-1 in top voice)
    # D minor context
    create_sample("century_14_ars_nova", [
        [('C5', 1), ('B4', 0.5), ('A4', 0.5), ('D5', 2)], # Top voice: C -> B-A (ornament) -> D
        [('A3', 1), ('G3', 1), ('F#3', 2)]  # Bottom voice
    ], time_sig='2/4', key_sig='d')

    # 15th Century: Renaissance (Triadic harmony, Fauxbourdon style - parallel 6/3 chords)
    create_sample("century_15_renaissance", [
        [('E5', 1), ('F5', 1), ('G5', 1), ('E5', 1)], # Top
        [('C5', 1), ('D5', 1), ('E5', 1), ('C5', 1)], # Middle
        [('A4', 1), ('B-4', 1), ('C5', 1), ('A4', 1)] # Bottom
    ], time_sig='4/4', key_sig='C')

    # 16th Century: High Renaissance (Palestrina style - Consonant polyphony)
    # Imitative entries
    create_sample("century_16_high_renaissance", [
        [('r', 2), ('G4', 1), ('A4', 1), ('B4', 2), ('C5', 2)], # Soprano enters later
        [('C4', 1), ('D4', 1), ('E4', 2), ('D4', 2), ('C4', 2)] # Alto enters first
    ], time_sig='4/4', key_sig='C')

    # 17th Century: Baroque (Basso Continuo / Circle of Fifths sequences)
    # Cycle of 5ths: Am - Dm - G - C
    create_sample("century_17_baroque", [
        [('C5', 1), ('F5', 1), ('B4', 1), ('E5', 1)], # Melody outlining chords
        [('A2', 1), ('D3', 1), ('G2', 1), ('C3', 1)]  # Bass root movement
    ], time_sig='4/4', key_sig='C')

    # 18th Century: Classical (Functional Harmony, Cadential 6/4)
    # I - IV - I6/4 - V7 - I
    create_sample("century_18_classical", [
        [('E4', 1), ('F4', 1), ('G4', 1), ('F4', 1), ('E4', 2)], # Melody
        [('C3', 1), ('F2', 1), ('G2', 1), ('G2', 1), ('C3', 2)], # Bass
        [('G3', 1), ('A3', 1), ('C4', 1), ('B3', 1), ('G3', 2)]  # Inner
    ], time_sig='6/4', key_sig='C') # Using 6/4 to fit durations

    # 19th Century: Romantic (Chromaticism, Diminished 7ths)
    # C - C#dim7 - Dm - G7b9 - C
    create_sample("century_19_romantic", [
        [('E4', 1), ('E4', 1), ('F4', 1), ('A-4', 1), ('G4', 2)], # Melody with chromatic passing
        [('C3', 1), ('C#3', 1), ('D3', 1), ('G2', 1), ('C3', 2)]  # Chromatic bass
    ], time_sig='4/4', key_sig='C')

    # 20th Century: Modern (Atonal / Whole Tone / Dissonant)
    # Whole tone scale usage
    create_sample("century_20_modern", [
        [('C4', 1), ('D4', 1), ('E4', 1), ('F#4', 1), ('G#4', 1), ('A#4', 1)],
        [('E3', 1), ('F#3', 1), ('G#3', 1), ('A#3', 1), ('C4', 1), ('D4', 1)]
    ], time_sig='6/4', key_sig=None)

    # 21st Century: Contemporary (Pop / Loop-based / Minimalism)
    # I - V - vi - IV (Axis of Awesome progression)
    create_sample("century_21_contemporary", [
        [('C4', 1), ('E4', 1), ('G4', 1), ('C5', 1)], # C
        [('G3', 1), ('B3', 1), ('D4', 1), ('G4', 1)], # G
        [('A3', 1), ('C4', 1), ('E4', 1), ('A4', 1)], # Am
        [('F3', 1), ('A3', 1), ('C4', 1), ('F4', 1)]  # F
    ], time_sig='4/4', key_sig='C')

if __name__ == "__main__":
    main()

