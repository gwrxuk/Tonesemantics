import music21
from music21 import chord, key, stream

class HarmonicAnalyzer:
    """
    Tools for analyzing musical grammar and syntax based on formal music theory.
    """
    
    @staticmethod
    def identify_key(score: stream.Score):
        """
        Estimates the key of a music21 stream.
        """
        return score.analyze('key')

    @staticmethod
    def get_chord_sequence(score: stream.Score):
        """
        Extracts a sequence of chords from a music21 stream.
        This is a simplified extraction method.
        """
        chords = []
        chord_stream = score.chordify()
        for c in chord_stream.recurse().getElementsByClass(chord.Chord):
            chords.append(c)
        return chords

    @staticmethod
    def roman_numeral_analysis(score: stream.Score):
        """
        Performs a basic Roman Numeral Analysis.
        """
        k = HarmonicAnalyzer.identify_key(score)
        chords = HarmonicAnalyzer.get_chord_sequence(score)
        rn_sequence = []
        
        for c in chords:
            # music21 can determine Roman Numerals relative to a key
            rn = music21.roman.romanNumeralFromChord(c, k)
            rn_sequence.append(rn.figure)
            
        return k, rn_sequence

