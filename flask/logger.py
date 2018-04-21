from __future__ import print_function
import sys

class Logger:
  
  @staticmethod
  def debug(message):
    print(message, file=sys.stderr)
  
  @staticmethod
  def info(message):
    print(message, file=sys.stderr)
  
  @staticmethod
  def warning(message):
    print(message, file=sys.stderr)
  
  @staticmethod
  def error(message):
    print(message, file=sys.stderr)