import glob
import os
from music21 import converter, instrument, note, chord

for file in glob.glob("model/midi_songs/*.mid"):
            
    print(file)
    try:
        midi = converter.parse(file)
    except:
        print("Error parsing midi!")
        os.remove(file)
        continue