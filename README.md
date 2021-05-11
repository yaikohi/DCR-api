# DCR-api v2
## DCR: Dominant color recognition.

A program that generates dominant colors of an image and returns the rgb colors in hexadecimal values.

The colours are generated using KMeans clustering.
The api was written with FastAPI.

To use this api I recommend using vscode and creating a new virtual environment.
To create a venv use
```terminal
python -m venv venv
```

To start the api use the following commands:
```terminal
python -m pip install requirements.txt
```
```terminal
$ cd api
hypercorn main:app --reload
```
You can now go to http://127.0.0.1:8000/api/docs to see the docs and test the various endpoints.
