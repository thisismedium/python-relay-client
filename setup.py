from __future__ import absolute_import
from setuptools import setup, find_packages

setup(
    name = 'relayio',
    version = '0.1',
    description = 'Relay.io Client',
    author = 'Medium',
    author_email = 'labs@thisismedium.com',
    license = 'BSD',
    keywords = 'rest relay.io',

    packages = list(find_packages(exclude=('examples', ))),
    install_requires = []
)
