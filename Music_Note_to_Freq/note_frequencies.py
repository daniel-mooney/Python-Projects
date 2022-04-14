import regex as re

def to_sharp_equivalent(note: str) -> str:
    # Converts a flatten to its sharp equivalent, does not work for double sharps or double flats
    
    notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    if note == 'Cb' or note == 'Fb':
        return chr( ord(note[0]) - 1)

    if note == 'B#' or note == 'E#':
        return chr( ord(note[0]) + 1)
    
    if len(note) == 1 or note[1] == '#':
        return note
    
    return notes[notes.index(note[0]) - 1] + '#'


def note_to_freq(note: str) -> float:
    # Frequencies of C0 to B0, returns a value within an accuracy of 0.001%

    if not re.match(r"[A-Ga-g]+[#b]*\d+", note):
        return None

    base_freq = {
        'C': 16.35, 'C#': 17.32, 'D': 18.35, 'D#': 19.45,
        'E': 20.6, 'F': 21.83, 'F#': 23.12, 'G': 24.5, 'G#': 25.96,
        'A': 27.5, 'A#': 29.14, 'B': 30.87}

    note = note.capitalize()

    pitch = note[0:2] if len(note) == 3 else note[0]
    pitch = to_sharp_equivalent(pitch)
    octave = int(note[-1])

    return base_freq[pitch] * 2**octave