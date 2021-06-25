#!/bin/python3
from notifypy import Notify
import sys

# get the message and title from cli
try:
    title = sys.argv[1]
    msg = sys.argv[2]
except:
    print('Usage:')
    print('\talert [title] [message]')
    sys.exit(1)

# call the class and send the message
nft = Notify()
nft.title = title
nft.message = msg
nft.icon = '/opt/alert/notify.png'
nft.send()
