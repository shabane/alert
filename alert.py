#!/bin/python3
from notifypy import Notify
import argparse

hlp_title = '''title of message'''
hlp_msg = ''' the message of notify'''

# define cli
cli = argparse.ArgumentParser(description='send a system notify')
cli.add_argument('title', type=str, help=hlp_title)
cli.add_argument('msg', type=str, help=hlp_msg)
args = cli.parse_args()

# get the message and title from cli
try:
    title = args.title
    msg = args.msg
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
