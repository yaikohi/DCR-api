# pioDash: dcr-api
This API provides endpoints that return RGB values of the dominant colours of an image.

# How to use
After copying the repo 

run
```terminal
$ python -m pip install requirements.txt
```
in the terminal to run its dependencies.

After you finished installing the dependencies you can run
```terminal
hypercorn main:app --reload
```
in the terminal to start the local server and inspect the API.

Go to http://127.0.0.1:8000/docs to inspect the swagger docs of this api. Here you can try out the different endpoints the API provides.

![Example](https://github.com/yaikohi/DCR-api/tree/Development/api/readme-images/howto1.gif)



## Note
Code contains a lot of comments. I suggest the [Better comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments) plugin voor vscode for proper readability.

## Sources
_Sources I used for learning how to make this product_
- [API - (stackoverflow) Best practices for structuring a fastAPI project](https://stackoverflow.com/questions/64943693/what-are-the-best-practices-for-structuring-a-fastapi-project)
- [API - FastAPI docs](https://fastapi.tiangolo.com/)

- [DCR - Dominant colors in an image using k-means clustering](https://buzzrobot.com/dominant-colors-in-an-image-using-k-means-clustering-3c7af4622036)
- [DCR - Finding the dominant colors in an image with k-means (large images)](https://ailephant.com/dominant-colors-in-image-with-k-means/#:~:text=The%20K%2Dmeans%20clustering%20algorithm%20defines%20a%20number%20K%20of,be%20used%20for%20other%20purposes.)