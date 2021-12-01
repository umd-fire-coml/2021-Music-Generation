import os
from music21 import converter, instrument, note, chord
import glob
from pathlib import Path
from generator import DataGenerator

def prepare():
    """
    return: 
    id_list: the filename extracted from path.
    n_vocab: number of possible notes from the dataset
    data_generator: 
    """
    id_list = []
    notes = set()
    g = glob.glob("model/midi_songs/*.mid")

    for file in g:
        p = Path(file).stem
        id_list.append(p)

    for item in g:
        try:
            midi = converter.parse(item)
        except:
            print("Error parsing midi!")
            continue
        notes_to_parse = None

        parts = instrument.partitionByInstrument(midi)

        if parts:  # file has instrument parts
            notes_to_parse = parts.parts[0].recurse()
        else:  # file has notes in a flat structure
            notes_to_parse = midi.flat.notes

        for element in notes_to_parse:
            if isinstance(element, note.Note):
                notes.add(str(element.pitch))
            elif isinstance(element, chord.Chord):
                notes.add('.'.join(str(n) for n in element.normalOrder))
    
    # get all pitch names
    pitchnames = sorted(set(item for item in notes))

    n_vocab = len(notes)

    dg = DataGenerator(id_list=id_list, batch_size=5, pitchnames=pitchnames)

    return n_vocab, dg

#prepare()
