![image](https://user-images.githubusercontent.com/17093016/145522974-9b977c45-7b94-41a9-b136-3cf7f6da0a23.png)

<h1> Team 6 - Music Generation </h1>

<p>
  Our project was to utilize an input of MIDI files to generate new music. We utilized a type of recurrent neural network called an LTSM model, which stands for Long Short-Term Memory network.
  Essentially, this type of model can efficiently learn and recognize long-term patterns. This sort of recognition is incredibly useful with music generation.
</p>

<h3> Model Architecture </h3>
<p>
  Our model is created by the model.py file. It starts out with a Sequential layer, and then we add the LTSM layer. We make sure that the input shape is 100. This means that that
  the model will receive a sequence of 100 notes for every song. The model's last layer is a softmax activation layer, so that we can tell the model to choose a single note to output.
  Essentially, our model will be predicting each note in order to eventually generate a song.
</p>

<h3> Using the Model </h3>
<iframe width="560" height="315" src="https://www.youtube.com/embed/m5mM3cCsIO0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<p>Try it out for yourself on <a href="https://drive.google.com/file/d/1rOWSiBm9kovAXVz6Hgv3fTxvnqr1a4D1/view?usp=sharing">Google Collab</a>!</p>

<h3> Directory Guide </h3>
<ol>
  <li>data</li>
  <ol>
   <li>data_download_script.py - Dataset Download Script for the LAKH-Cleansed Dataset</li>
   <li>data_download_small.py - Dataset Download Script for our own custom Dataset (use this!)</li>
  </ol>
  <li>model</li>
  <ol>
   <li>logs - Training logs</li>
   <li>model - For running training</li>
   <li>weights - For running testing via collab</li>
   <li>clean.py - Script to clean up workspace</li>
   <li>data_prep.py - script to prepare workspace</li>
   <li>model.py - script to build model</li>
   <li>predict.py - script to test model</li>
   <li>test_output.mid - an example output file from the model</li>
   <li>train.py - script to train model</li>
   <li>train_model.ipynb - Jupyter Notebook to train model</li>
   <li>weights.hdf5 - Most recent weights for the model</li>
  </ol>
<li>.gitignore - Ignored files</li>
<li>requirements.txt - Required libraries!</li>
</ol>

<h3> Setting up the environment </h3>
<p> Just install whatever is in the requirements.txt using pip. Make sure you are using Python 3.9.6! </p>
<code> pip install -r requirements.txt </code>

<h3> Setting up the data </h3>
<p> At the moment, this model only works with our curated dataset as it directly loads everything into memory rather than using a data generator. Due to this, you must use the
  data_download_small.py script found in the data folder. Just import it and call the function small() and it will download and unzip. </p>

```
from data_download_small.py import small
small()
```
<h3> Training </h3>
<p> 
Training can be done using the provided jupyter notebook. Everything that is required should be found in the inner model folder that is inside the outter model folder. When you clone this repository, just run the jupyter notebook and you should be training. You will have the option to change batch size and epochs within it. The jupyter notebook should also load the weights.hdf5 file, which is our most recently trained weights.
  
<h3> Testing </h3>
To test, use <a href="https://drive.google.com/file/d/1rOWSiBm9kovAXVz6Hgv3fTxvnqr1a4D1/view?usp=sharing">Google Collab</a>. Use this collab, and run the first cell. Then, overwrite the weights.hdf5 file that it clones with your own if you have it. Then, run the rest of the cells. It will spit out an output file and visualize it.
</p>
