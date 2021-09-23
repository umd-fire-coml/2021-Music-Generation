import os

# install necessary packages to download package and view data
os.system('pip install gdown')
os.system('pip install pypianoroll')

import gdown
import tarfile

# url of where the .tar data file is
file_url = 'https://drive.google.com/uc?id=11rxrGaQbfTW-WC0k2GlR9YDAT-UxIb4O'
output = 'lpd_cleansed.tar'

# download the .tar file
gdown.download(file_url, output, quiet=False)
    
# open and extract the .tar file
tar = tarfile.open(output)
tar.extractall()
# extraction takes a while so just wait until it prints done
tar.close()
print("Done!")

# delete the .tar file from the system
os.system('rm lpd_cleansed.tar')

print("Data is in lpd/lpd_cleansed")