import logging
from .Log4Mongo_wrapper import get_handler


class PickleableLogger(logging.Logger):
  """
  Custom pickleable Logger class.
  """

  def __getstate__(self):
    """
    Remove unpickleable handlers before dumping binary.
    """
    state = self.__dict__.copy()
    state['handlers'] = []
    return state

  def __setstate__(self, state):
    """
    Add back handlers after loading binary.
    """
    self.__dict__.update(state)
    self.addHandler(get_handler())

  @classmethod
  def convert_to_pickleable(cls, obj):
    """
    Convert a normal logger to a pickleable logger.

    Magic!
    """
    obj.__class__ = PickleableLogger


def setup_logger(name, level=logging.DEBUG):
  """Function setup as many loggers as you want."""
  logger = logging.getLogger(name)
  PickleableLogger.convert_to_pickleable(logger)
  logger.setLevel(level)
  logger.addHandler(get_handler())
  return logger


if __name__ == "__main__":
  logger = setup_logger('package_test', logging.DEBUG)
  logger.debug('testing logger')

