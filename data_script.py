# download "lpd-cleansed" from https://salu133445.github.io/lakh-pianoroll-dataset/dataset
# unzip the .tar file and load the lpd folder into 2021-Music-Generation folder

# install Pypianoroll by using "pip install pypianoroll" -> mac/linux only (maybe windows idk)

# example of use

import pypianoroll as pr

new = pr.load("lpd/lpd_cleansed/A/A/A/TRAAAGR128F425B14B/b97c529ab9ef783a849b896816001748.npz")

pr.plot_multitrack(new, pr.plot(new))