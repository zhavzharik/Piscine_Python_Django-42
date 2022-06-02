#!/bin/sh

PYTHON_PATH="/Users/abridger/.brew/bin/python3"


#create environment and activate it
$PYTHON_PATH -m venv django_venv
source django_venv/bin/activate

python -m pip install --upgrade pip

#display which pip version it uses
python -m pip --version

#install logs, install the path.py development version from its GitHub repo
python -m pip install -r requirements.txt





