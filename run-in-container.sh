#!/bin/bash
docker run --rm -it -p "0.0.0.0:8000:8000" -v "$PWD:/server" python:3.6 bash "/server/run.sh"
