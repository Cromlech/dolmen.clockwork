# -*- coding: utf-8 -*-

from grokcore.component import Adapter, context, provides, name
from cromlech.browser import IRequest
from .i18n import date_formatter, date_parser
from .i18n import datetime_formatter, datetime_parser
from .i18n import time_formatter, time_parser
from .interfaces import IFormDateManager, IFormTimeManager


class DefaultFormDateManager(Adapter):
    name('date')
    context(IRequest)
    provides(IFormDateManager)
    size = "short"

    def format(self, value):
        return date_formatter(self.context, value, self.size)

    def parse(self, value):
        return date_parser(self.context, value, self.size)


class DefaultFormDatetimeManager(Adapter):
    name('dateTime')
    context(IRequest)
    provides(IFormDateManager)
    size = "short"

    def format(self, value):
        return datetime_formatter(self.context, value, self.size)

    def parse(self, value):
        return datetime_parser(self.context, value, self.size)


class DefaultFormTimeManager(Adapter):
    context(IRequest)
    provides(IFormTimeManager)
    size = "short"

    def format(self, value):
        return time_formatter(self.context, value, self.size)

    def parse(self, value):
        return time_parser(self.context, value, self.size)
