"""relayio -- Python client interface to <http://relay.io/>."""

from __future__ import absolute_import
import httplib, urllib, urlparse, json

class RelayIO(object):
    """RelayIO -- REST client"""

    def __init__(self, feedUri, insertKey):
        self.insertKey = insertKey
        self.apiUri = urlparse.urlparse(feedUri)

    def insert(self, data):
        params = urllib.urlencode({
            'insertkey': self.insertKey,
            'payload': json.dumps(data)
        })

        client = httplib.HTTPConnection(self.apiUri.netloc)
        client.request('POST', self.apiUri.path, params, {
            'Content-Type': 'application/x-www-form-urlencoded'
        })

        response = client.getresponse()
        if response.status != 200:
            raise RelayError(response.read())

class RelayError(RuntimeError):
    pass
