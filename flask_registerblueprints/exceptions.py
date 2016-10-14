"""Module contains custom exceptions for this package.
"""


class Error(Exception):
    """Base-class for all exceptions raised by this package."""


class InvalidDirectory(Error):
    """Invalid directory path; does not exist or is not directory"""
