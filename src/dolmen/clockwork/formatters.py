# -*- coding: utf-8 -*-

from grokcore.component import Adapter, context, provides
from cromlech.browser import IRequest
from .i18n import date_localizer, date_parser
from .interfaces import IFormDateManager


class IDefaultFormDateManager(Adapter):
    context(IRequest)
    provides(IFormDateManager)

    def format(self, value):
        return date_localizer(self.context, value)

    def parse(self, value):
        return date_parser(self.context, value)
