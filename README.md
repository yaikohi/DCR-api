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
You can now go to http://127.0.0.1:8000/docs to see the docs.
or navigate to the other endpoints:

https://127.0.0.1:8000/{company_name}/colors
https://127.0.0.1:8000/{company_name}/
https://127.0.0.1:8000/

where company_name can be any of the company names found in the https://127.0.0.1:8000/ endpoint.
