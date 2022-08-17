# How to release this lib
For details see the description in

https://packaging.python.org/en/latest/tutorials/packaging-projects/

## 1. Generate the lib
as defined in pyproject.toml
```
python -m build
```

## 2. Publish to PyPi
upload the generated package files from the dist folder
```
python -m twine upload dist/*
```

## 3. Installing the latest uploaded package
```
python -m pip install mdrunner
```
