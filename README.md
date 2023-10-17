# Triangle example for QA class. Python edition. 

This is a flask application, that repeats the triangle java code. 
It will be used to understand the unitttest module in Python. 
You need python3 & pip installed and on the path. 

## How to use it.

Clone the repository: 

```
git clone https://github.com/hfierros/trngl_python.git
```

To avoid pip to affec the whole local environment, create a python environment: 

```
virtualenv .venv
```

Enable the environment: 
On linux/MAC:
```
source .venv/bin/activate
```
On windows: 
```
.\.venv\Scripts\activate
```

And then install all the dependencies with pip: 
```
pip install -r requirements.txt
```

Now configure flask, by setting the FLASK_APP environment variable:
On linux/MAC:
```
export FLASK_APP=flasky.py
```
On windows:
```
set FLASK_APP=flasky.py
```

And now run the app: 
```
flask run
```


