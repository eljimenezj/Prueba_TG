# Trascender Global - Image Classification
Repo with the technical test results

The steps of the technical test are described below.

1. Step 1

It was organized in folders by the type of class that the image is. This was done in the train, validation and test folders. For this the script called: 0_FolderStructure.py was used. You must rewrite the path with your address where the unzipped folder of the images is located

2. Step 2

Google Colaboratory was used to develop the classification model, for this, the images were uploaded to Google Drive and the model was built using Tensorflow and keras. The model was then saved locally to be used in the streamlit app.

3. Step 3

The image classification app is built using the streamlit. The previously trained model is loaded and deployed locally at http://localhost:8505/.

# How to use this repo

Important: Due to the weight of the trained model, it could not be uploaded to the personal github, so gitlab could be used. However, for this exercise the file uploaded is shared publicly on Google drive that you can download through this link (you must save it in this repo when you download it):
Link model: https://drive.google.com/drive/folders/1zCYERJkrgcR38afeTBnVH32FsuzuMJtR?usp=sharing

If you want to replicate the exercise you can:

Create an new environment with conda promt, called for example imageclass: 
```
conda create -n imageclass python=3.6
```
Then, active your new environment:
```
conda activate imageclass
```
 Install the libraries to use, first install streamlit:
```
pip install streamlit
```
Then, tensorflow, and all the others requirements
```
pip install tensorflow
pip install ……
```
Finally you must run the application with streamlit
```
streamlit run app.py
```

# Requirements

* python==3.6
* tensorflow==2.4.1
* image==1.5.33
* Keras == 2.4.3
* Keras_Preprocessing == 1.1.2
* Pillow == 8.1.0
* joblib == 1.0.1
* matplotlib == 3.3.4
* opencv_python == 4.4.0.46
* pandas == 1.2.2
* scikit_learn == 0.23.2
* streamlit == 0.76.0
* tensorflow == 2.3.0
* numpy == 1.19.2


The list of libraries is in the file requirements.txt.

For any comments or suggestions please write: eljimenezj@gmail.com

**Edgar Jimenez, Feb 2021**

