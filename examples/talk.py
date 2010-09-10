#!/usr/bin/env python

"""talk.py post-to-url insert-key message

This talk script finds your username in the environment and reads a
message from standard input.  It packages this information into a
dictionary, then adds it to your relay.

For example:

> talk.py http://api.relay.io/insert/MY-FEED-ID MY-INSERT-KEY 'Hello, relay!'
"""

import os, sys, relayio

def main(feedUri=None, insertKey=None, message=None):
    if not (feedUri and insertKey and message):
        usage()

    relay = relayio.RelayIO(feedUri, insertKey)
    relay.insert({
        'who': os.environ.get('USER', 'anonymous'),
        'said': message
    })

    print 'Message sent.'

def usage():
    print __doc__
    sys.exit(1)

if __name__ == '__main__':
    main(*sys.argv[1:])
