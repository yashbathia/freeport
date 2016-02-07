# -*- coding: utf-8 -*-

__author__ = 'Yash Bathia'
__email__ = 'yash.bathia@yahoo.com'
__version__ = '0.1.0'
import json
import os

from freeport import *


_metadata_file = os.path.join(
    os.path.dirname(__file__),
    'package_metadata.json'
)

if os.path.exists(_metadata_file):  # pragma: no cover
    with open(_metadata_file) as fh:
        _package_metadata = json.load(fh)
        __version__ = _package_metadata['version']
else:
    __version__ = '0.0.0'  # pragma: no cover
