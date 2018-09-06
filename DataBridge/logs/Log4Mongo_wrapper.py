import os
import logging
from log4mongo.handlers import BufferedMongoHandler


def get_handler():
  '''
  Return a log4mongo logging handler.

  Use docker networking if in a docker container.
  Otherwise use a mongodb that exists on the localhost
  '''
  if os.path.exists('/.dockerenv'):
    host = 'mongo'
  else:
    host = 'localhost'

  # Buffered handler writes logs periodically, to prevent frequent write-locks
  handler = BufferedMongoHandler(host=host, port=27017,
                                 buffer_size=1000,
                                 buffer_periodical_flush_timing=10.0,
                                 buffer_early_flush_level=logging.CRITICAL)
  return handler

