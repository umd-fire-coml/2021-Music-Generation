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
<p> Insert YouTube Link here </p>
<p>Try it out for yourself on <a href="https://drive.google.com/file/d/1rOWSiBm9kovAXVz6Hgv3fTxvnqr1a4D1/view?usp=sharing">Google Collab</a>!</p>

<h3> Directory Guide </h3>
<ol>
  <li>data</li>
  <ol>
   <li>data_download_script.py - Dataset Download Script for the LAKH-Cleansed Dataset</li>
   <li>dat_download_small.py - Dataset Download Script for our own custom Dataset (use this!)</li>
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
