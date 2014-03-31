# -*- coding: utf-8 -*-

from zope.interface import Interface


class IFormDateManager(Interface):

    def format(value):
        """Returns a formatted string from a date object.
        """

    def parse(value):
        """Returns a date object from the string value.
        """
