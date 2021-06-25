#!/bin/bash

mkdir /opt/alert
cp ./alert.py /opt/alert/alert.py
chmod +x /opt/alert/alert.py
ln /opt/alert/alert.py /bin/alert
