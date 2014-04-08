# -*- coding: utf-8 -*-

from grokcore.component import Adapter, context, provides
from cromlech.browser import IRequest
from .i18n import date_formatter, date_parser
from .i18n import time_formatter, time_parser
from .interfaces import IFormDateManager, IFormTimeManager


class IDefaultFormDateManager(Adapter):
    context(IRequest)
    provides(IFormDateManager)

    def format(self, value):
        return date_formatter(self.context, value)

    def parse(self, value):
        return date_parser(self.context, value)


class IDefaultFormTimeManager(Adapter):
    context(IRequest)
    provides(IFormTimeManager)

    def format(self, value):
        return time_formatter(self.context, value)

    def parse(self, value):
        return time_parser(self.context, value)
