#!/bin/bash
DIRECTORY=`dirname $0`
cd $DIRECTORY
pip3 install -r requirements.txt --user
python3 manage.py runserver 0.0.0.0:8000
