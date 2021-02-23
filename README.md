# Prueba_TG
Repo with the technical test results

The steps of the technical test are described below.

1. Step 1

It was organized in folders by the type of class that the image is. This was done in the train, validation and test folders. For this the script called: 0_FolderStructure.py was used. You must rewrite the path with your address where the unzipped folder of the images is located

2. Step 2

Google Colaboratory was used to develop the classification model, for this, the images were uploaded to Google Drive and the model was built using Tensorflow and keras. The model was then saved locally to be used in the streamlit app.

3. Step 3

The image classification app is built using the streamlit. The previously trained model is loaded and deployed locally at http://localhost:8505/.
