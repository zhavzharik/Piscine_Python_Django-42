#!/bin/sh

PYTHON_PATH="/Users/abridger/.brew/bin/python3"
VENV_NAME="django_venv_d07"

#create environment and activate it
$PYTHON_PATH -m venv $VENV_NAME
source $VENV_NAME/bin/activate

python3 -m pip install --upgrade pip

#display which pip version it uses
python3 -m pip --version

#install requirements
pip3 install --force-reinstall -r requirements.txt

