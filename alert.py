#!/bin/python3
from notifypy import Notify
import sys

# get the message and title from cli
title = sys.argv[0]
msg = sys.argv[1]

# call the class and send the message
nft = Notify()
nft.title = title
nft.message = msg
nft.send()
