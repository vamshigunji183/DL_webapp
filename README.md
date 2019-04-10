# Web app - Classification of dogs and cats - FLASK, PYTHON, CNN

#### pre-requisites
[python](https://www.python.org/downloads/), [git](https://git-scm.com/downloads), [pip](https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation)

#### instructions to use this application
* `git clone` [https://github.com/vamshigunji183/DL_webapp](https://github.com/vamshigunji183/DL_webapp)
* `pip install -r requirements.txt`

Go to the directory `../DL_webapp`
Edit the `predict_app.py` file as show below.
* Download the train model here to the current directory.
* Replace the `<--TRAINED MODEL--.h5>` with the downloaded model name. [In this case - [VGG16_cats_and_dogs.h5](https://drive.google.com/file/d/1jtJbWLWdU0Dr528fEcxV2a7BiJOOgzbG/view?usp=sharing)]

In the command terminal `cd` to the current directory
* windows- `>>set FLASK_APP=predict_app.py`
   UNIX- `$ export FLASK_APP=predict_app.py`
* `flask run --host=0.0.0.0`

Open the web browser
* Enter the url - `http://localhost:5000/static/predict.html` or [click here](http://localhost:5000/static/predict.html)

Use the sample images or ANY dogs or cats images `png` format

Example:

![alt text](https://github.com/vamshigunji183/DL_webapp/readme/dog-prediction.JPG "DOG PREDICTION EXAMPLE") ![alt text](https://github.com/vamshigunji183/DL_webapp/readme/dog-prediction-1.JPG "DOG PREDICTION EXAMPLE")

![alt textalt text](https://github.com/vamshigunji183/DL_webapp/readme/cat-prediction.JPG "CAT PREDICTION EXAMPLE")
![alt text](https://github.com/vamshigunji183/DL_webapp/readme/cat-prediction-1.JPG "CAT PREDICTION EXAMPLE")
