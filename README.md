# flag_detection
Code for flag detection model for the IMAV-2019 Indoors.<br>
You can read the problem statement of IMAV-19 Indoors [here](https://imav2019.org/).<br>
One part of the problem statement was to detect a flag in a flag stand by the drone, and during the course of the mission, it will get a package which it have to drop at one of the three conveyer belts, which would have the same flag which was shown to the drone in the beginning of the mission.<br>
This flag detection part was done with the help of this model.<br>
The `NewFlagData` folder contains the train and test data in separate folders and the inside them all the images are segregated into folders for different countries, which participated in the competition.<br>
The `savedModel` folder contains the saved model weights and also the whole model for inferencing.<br>
The `flag_detect.ipynb` contains the training code for the model, here i used a conv net with custom built architecture and got around <b>82%</b> test set accuracy.<br>
The `augment.py` contains the code for augmenting the images which i downloaded from the internet and create multiple copies for training dataset. 
