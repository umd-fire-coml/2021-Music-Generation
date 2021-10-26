import os
import glob

def cleanup():

    # assign directory
    directory = 'weights'
    files = []
    max = 0
    string = "null"
    counter = 0
    weight = "weights/"
    

    if len(os.listdir(directory)) != 0:
        # iterate over files in
        # that directory
        for filename in os.listdir(directory):
            files.append(filename.split('-'))

        for file in files:
            if int(file[2]) > max:
                max = int(file[2])
                string = file
            counter += 1

        for word in string:
            weight += word+"-"
        weight = weight[:-1]

        os.replace(weight, "weights.hdf5")

        for file in os.listdir(directory):
            os.remove("weights/"+file)