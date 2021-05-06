#!/usr/bin/env bash
cd ..

PWD=`pwd`
LANG=ko_KR.utf8
PROCESS_NAME=`basename ${PWD}`
PYTHON_PATH="python"
# PYTHON_PATH="/usr/local/bin/python3.6"

${PYTHON_PATH} main.py $@ 2>> ./logs/${PROCESS_NAME}.err 
