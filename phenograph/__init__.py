from phenograph.cluster import cluster
from phenograph.classify import classify

import logging
from logging import NullHandler
logging.getLogger(__name__).addHandler(NullHandler())