from music21 import stream, meter, key, chord, note, midi, instrument

def create_tonal_sample(output_path: str):
    """
    Creates a simple 4-part harmony sample characteristic of the Western tonal system.
    Progression: I - vi - IV - V7 - I in C Major.
    """
    score = stream.Score()
    score.insert(0, metadata.Metadata())
    score.metadata.title = "Tonal Grammar Sample"
    score.metadata.composer = "Tonesemantics AI"

    # Define parts
    soprano = stream.Part()
    alto = stream.Part()
    tenor = stream.Part()
    bass = stream.Part()

    soprano.id = 'Soprano'
    alto.id = 'Alto'
    tenor.id = 'Tenor'
    bass.id = 'Bass'

    # Assign instruments (Piano for simplicity)
    for p in [soprano, alto, tenor, bass]:
        p.insert(0, instrument.Piano())

    # Key and Time Signature
    k = key.Key('C')
    ts = meter.TimeSignature('4/4')
    
    for p in [soprano, alto, tenor, bass]:
        p.insert(0, k)
        p.insert(0, ts)

    # Chord Progression: C -> Am -> F -> G7 -> C
    # Voice Leading (approximate for demonstration)
    
    # 1. C Major (I)
    # S: E5, A: C5, T: G4, B: C3
    soprano.append(note.Note('E5', quarterLength=1.0))
    alto.append(note.Note('C5', quarterLength=1.0))
    tenor.append(note.Note('G4', quarterLength=1.0))
    bass.append(note.Note('C3', quarterLength=1.0))

    # 2. A Minor (vi)
    # S: E5, A: C5, T: A4, B: A2
    soprano.append(note.Note('E5', quarterLength=1.0))
    alto.append(note.Note('C5', quarterLength=1.0))
    tenor.append(note.Note('A4', quarterLength=1.0))
    bass.append(note.Note('A2', quarterLength=1.0))

    # 3. F Major (IV)
    # S: F5, A: C5, T: A4, B: F2
    soprano.append(note.Note('F5', quarterLength=1.0))
    alto.append(note.Note('C5', quarterLength=1.0))
    tenor.append(note.Note('A4', quarterLength=1.0))
    bass.append(note.Note('F2', quarterLength=1.0))

    # 4. G Dominant 7th (V7)
    # S: D5, A: B4, T: G4, B: G2
    soprano.append(note.Note('D5', quarterLength=1.0))
    alto.append(note.Note('B4', quarterLength=1.0))
    tenor.append(note.Note('G4', quarterLength=1.0))
    bass.append(note.Note('G2', quarterLength=1.0))

    # 5. C Major (I) - Resolution
    # S: C5, A: G4, T: E4, B: C3
    soprano.append(note.Note('C5', quarterLength=4.0)) # Whole note
    alto.append(note.Note('G4', quarterLength=4.0))
    tenor.append(note.Note('E4', quarterLength=4.0))
    bass.append(note.Note('C3', quarterLength=4.0))

    # Add parts to score
    score.insert(0, soprano)
    score.insert(0, alto)
    score.insert(0, tenor)
    score.insert(0, bass)

    # Write to MIDI
    fp = score.write('midi', fp=output_path)
    print(f"Generated tonal sample at: {fp}")

if __name__ == "__main__":
    import os
    # Ensure directory exists
    output_dir = os.path.join(os.path.dirname(__file__))
    output_file = os.path.join(output_dir, "tonal_sample.mid")
    
    from music21 import metadata # Imported here to be available in function if needed, but better at top
    
    create_tonal_sample(output_file)

