#!/bin/bash

[ -d venv ] || virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
echo 'now run: source venv/bin/activate'

