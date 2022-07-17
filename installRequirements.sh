#!/bin/bash

sudo apt update
sudo apt install  python-is-python3 python3-pip python3-testresources
sudo pip3 install --target=/usr/lib/python3/dist-packages --upgrade -r requirements.txt
