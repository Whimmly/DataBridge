from .setup_logger import setup_logger
import logging


log_grapherror = setup_logger("GraphError", logging.ERROR)


class GraphError(Exception):
  def __init__(self, message, errors):
    super(GraphError, self).__init__(message)
    log_grapherror.error(message)

