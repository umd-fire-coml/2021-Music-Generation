import numpy as np
import os
from numpy import random
from tensorflow.keras.utils import Sequence
from music21 import converter, instrument, note, chord
from tensorflow.keras.utils import to_categorical

import glob, numpy

class DataGenerator(Sequence):
    '''this is a random data generator, edit this data generator to read data from dataset folder and return a batch with __getitem__'''

    def __init__(self, pitchnames, id_list, batch_size=100):
        self.batch_size = batch_size
        self.n_dataset_items = len(id_list)
        #self.indexes = np.arange(self.n_dataset_items)
        self.filepaths = os.listdir("model/midi_songs/")
        self.pitchnames = pitchnames
        self.id_list = id_list
        self.access_time = 0
        self.sequence_length = 100
        self.on_epoch_end()

    def __len__(self):
        """Denotes the number of batches per epoch
        :return: number of batches per epoch
        """
        return int(np.floor(self.n_dataset_items / self.batch_size))

    def __getitem__(self, index):
        """Generate one batch of data
        :param index: index of the batch
        :return: x_batch and y_batch
        """

        """
        items = []
        notes = []
        sequence_length = self.sequence_length

        indexes = self.indexes[index * self.batch_size : (index+1) * self.batch_size]

        for i in range(self.batch_size):
            items.append(self.filepaths[indexes[i]])

        for file in items:
            data = "model/midi_songs/"+file
            print(data)
            try:
                midi = converter.parse(data)
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
                    notes.append(str(element.pitch))
                elif isinstance(element, chord.Chord):
                    notes.append('.'.join(str(n) for n in element.normalOrder))
        """
        notes = []
        midi = converter.parse("model/midi_songs/"+self.curr_file+".mid")
        notes_to_parse = None

        parts = instrument.partitionByInstrument(midi)
        
        if parts:  # file has instrument parts
            notes_to_parse = parts.parts[0].recurse()
        else:  # file has notes in a flat structure
            notes_to_parse = midi.flat.notes

        for element in notes_to_parse:
            if isinstance(element, note.Note):
                notes.append(str(element.pitch))
            elif isinstance(element, chord.Chord):
                notes.append('.'.join(str(n) for n in element.normalOrder))
        # get all pitch names
        pitchnames = sorted(set(item for item in notes))

        # create a dictionary to map pitches to integers
        note_to_int = dict((note, number) for number, note in enumerate(pitchnames))
        network_input = []
        network_output = []
        n_vocab = len(set(notes))
        print("n_vocab: {}".format(n_vocab))


        # create input sequences and the corresponding outputs
        for i in range(0, len(notes) - self.sequence_length, 1):
            sequence_in = notes[i:i + self.sequence_length]
            sequence_out = notes[i + self.sequence_length]
            network_input.append([note_to_int[char] for char in sequence_in])
            network_output.append(note_to_int[sequence_out])
        
        n_patterns = len(network_input)

        # reshape the input into a format compatible with LSTM layers
        network_input = numpy.reshape(network_input, (n_patterns, self.sequence_length, 1))

        # normalize input
        network_input = network_input / float(n_vocab)
        network_output = to_categorical(network_output)
        
        """
        start = random.randint(0, self.n_dataset_items - self.batch_size)

        network_input, network_output = self.prepare(start, self.batch_size)
        """
        # Return batch data
        return network_input, network_output

    def on_epoch_end(self):
        """Shuffle indexes after each epoch
        """
        if self.access_time <= 0:
            self.curr_file = self.id_list[np.random.randint(0, len(self.id_list))]
            midi = converter.parse("model/midi_songs/"+self.curr_file+".mid")
            notes_to_parse = None
            parts = instrument.partitionByInstrument(midi)
            if parts:  # file has instrument parts
                notes_to_parse = parts.parts[0].recurse()
            else:  # file has notes in a flat structure
                notes_to_parse = midi.flat.notes
            self.song_len = len(notes_to_parse)
            self.access_time = int(self.song_len / (self.sequence_length * self.batch_size))

        #np.random.shuffle(self.indexes)

    def prepare(self, index, batch_size):
        notes = []
        sequence_length = 100

        counter = -1
        for file in glob.glob("model/midi_songs/*.mid"):
            counter += 1
            if counter < index or counter >= index+batch_size:
                continue
            
            print(file)
            try:
                midi = converter.parse(file)
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
                    notes.append(str(element.pitch))
                elif isinstance(element, chord.Chord):
                    notes.append('.'.join(str(n) for n in element.normalOrder))

        # get all pitch names
        pitchnames = sorted(set(item for item in notes))

        # create a dictionary to map pitches to integers
        note_to_int = dict((note, number) for number, note in enumerate(pitchnames))
        network_input = []
        network_output = []
        n_vocab = len(set(notes))
        print("n_vocab: {}".format(n_vocab))


        # create input sequences and the corresponding outputs
        for i in range(0, len(notes) - sequence_length, 1):
            sequence_in = notes[i:i + sequence_length]
            sequence_out = notes[i + sequence_length]
            network_input.append([note_to_int[char] for char in sequence_in])
            network_output.append(note_to_int[sequence_out])
        
        n_patterns = len(network_input)

        # reshape the input into a format compatible with LSTM layers
        network_input = numpy.reshape(network_input, (n_patterns, sequence_length, 1))

        # normalize input
        network_input = network_input / float(n_vocab)
        network_output = to_categorical(network_output)

        return network_input, network_output