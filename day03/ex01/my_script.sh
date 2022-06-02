#!/bin/sh

PYTHON_PATH="/Users/abridger/.brew/bin/python3"
URL_PATH_PY="https://github.com/jaraco/path.git"

#create environment and activate it
$PYTHON_PATH -m venv local_lib
source local_lib/bin/activate

python -m pip install --upgrade pip

#display which pip version it uses
python -m pip --version

#install logs, install the path.py development version from its GitHub repo
python -m pip install --log "pip_install.log" --force-reinstall git+$URL_PATH_PY


echo "**************** execute program ****************"
python3 my_program.py


