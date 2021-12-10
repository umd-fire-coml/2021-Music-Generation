import os
import zipfile
import gdown
import tarfile

def small():

    # install necessary packages to download package and view data
    os.system('pip install gdown')

    # url of where the .tar data file is
    file_url = 'https://drive.google.com/file/d/1f-fwh5yN93ZhBhox8vQpOtHftog2TaBT/view?usp=sharing'
    output = 'midi_songs.zip'

    # download the .tar file
    os.system('gdown https://drive.google.com/u/1/uc?id=1f-fwh5yN93ZhBhox8vQpOtHftog2TaBT&export=download')
    #gdown.download(file_url, output, quiet=False)

    print("Done!")

    with zipfile.ZipFile("midi_songs.zip", 'r') as zip_ref:
        zip_ref.extractall("model/")

    os.system('rm midi_songs.zip')