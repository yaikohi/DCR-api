# DCR-api v2
#### *(SCHOOL PROJECT)* 
## DCR: Dominant color recognition.

A program that generates dominant colors of an image and returns the rgb colors in hexadecimal values.

The colours are generated using KMeans clustering.
The api was written with FastAPI.

To use this api I recommend using vscode and creating a new virtual environment.
To create a venv use
```terminal
$ python -m venv venv
```

To start the api use the following commands:
```terminal
$ python -m pip install requirements.txt
```
```terminal
$ hypercorn main:app --reload
```
You can now go to http://127.0.0.1:8000/api/docs to see the docs and test the various endpoints.

## Folders

### _$ (root folder)_
[Procfile](Procfile) - for hosting the api on heroku.
[dockerfile](dockerfile) - for creating a docker-image.

### _Core_
Contains config.py with basic fastapi configurations.

### _Routes_
Contains the router and the routes for the api. 
- [piodash.py](/routes/piodash.py) contains the routes for the piodash project.
- [images.py](/routes/images.py) contains unfinished code.
- [router.py](/routes/router.py) puts all the routes together and provides the variable used in main.py

### _Services_
Contains functions used by the endpoints.
- [dcr_test.py](/services/) unittest for [dcr.py](/services/dcr.py)
- [dcr.py](/services/dcr.py) dominant color recognition function using Kmeans.
- [fetch_data.py](/services/fetch_data.py) contains various fetch functions.

### _v1_
Contains v1 of this api.
