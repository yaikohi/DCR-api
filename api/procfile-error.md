# Heroku problems
following the tutorial on the flask/python example I encountered some problems.


## Problem 1:
```Terminal
$ git push heroku main 
error: src refspec main does not match any
error: failed to push some refs to 'https://git.heroku.com/quiet-reef-14961.git'
```
Solution:
instead of
```Terminal
git push heroku main 
```

use 
```Terminal
git push heroku master
```




## Problem 2:
```Terminal
(venv) $ heroku ps:scale web=1 
Scaling dynos... !
 !    Couldn't find that process type (web).
```
Solution: https://stackoverflow.com/a/53184918
