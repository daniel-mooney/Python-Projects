# Music to Note Frequency
This project contains two parts...a python script that encodes and writes a list of tuples containing musical note information to a binary file as well as the the functions found in `note_frequencies.py` to help achieve this.

## note_frequencies.py
This module converts a string representing a note in the form `<note_name><octave>` into a frequency in Hertz. It is designed to handle only single flats and sharps. Anything beyond a single sharp or flat (i.e. double sharps) should not be passed into `note_to_freq()`.

## music_binary_file.py
This script makes use of the `note_frequencies` module to convert a list of tuples in the form of (`<note>`, `<duration>`) into a binary file. Duration is the beats of a note scalled by 4 (i.e. 4 represents a crotchet). A duration number less than 1 should not be used.

The binary output is structured into a frame consisting of 3 bytes; 2 bytes for the note frequency and one byte for the note duration. The BPM (beats per minute) of the song being written is the first integer written to the binary file.