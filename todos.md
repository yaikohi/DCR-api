# TODOS
- Change the GET-request to a Asynchronous request
- Add explanation in docstring about the fetch_and_save_image() function.
    - Why download an image, load it as a BytesIO object, and proceed to read it as a PIL image object? Aren't there better ways to go about this?
- Add error handlings to the HTTP requests.
- Double check the docstrings for formatting
- Simplify code (line 34 to 59: 

```Python 
logos_dict = {company['name']: f"https://dashboard-pio.herokuapp.com{company['logo']}" for company in db}
```
- Add security to the public API (dashboard-pio.herokuapp)
- Change global variables to local variables to prevent issues