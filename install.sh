#!/bin/bash
pip3 install notify-py
mkdir /opt/alert
cp ./alert.py /opt/alert/alert.py
cp ./notify.png /opt/alert/
chmod +x /opt/alert/alert.py
ln /opt/alert/alert.py /bin/alert
