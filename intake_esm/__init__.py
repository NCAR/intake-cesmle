#!/usr/bin/env python
"""Top-level module for intake_esm."""
from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions

from .config import set_options, get_options
from .manage_collections import CESMCollections
from .core import CesmSource, CesmMetadataStoreCatalog