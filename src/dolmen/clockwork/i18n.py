# -*- coding: utf-8 -*-

import datetime
import pytz
from cromlech.i18n import ILanguage
from zope.i18n.locales import LocaleFormat, locales


BASE = pytz.utc
PARIS = pytz.timezone('Europe/Paris')
DATETIME_SHORT = '%Y-%m-%d %H:%M'


# This needs proper registration
# And localization.
base_format = LocaleFormat()
base_format.pattern = u'dd/MM/yyyy'


def date_parser(request, date, size='short'):
    language = ILanguage(request, None)
    locale = locales.getLocale(language=language)
    formatter = locale.dates.getFormatter('date', length=size)
    return formatter.parse(date)


def date_formatter(request, date, size='short'):
    language = ILanguage(request, None)
    locale = locales.getLocale(language=language)
    formatter = locale.dates.getFormatter('date', length=size)
    return formatter.format(date)


def time_parser(request, time, size='short'):
    language = ILanguage(request, None)
    locale = locales.getLocale(language=language)
    formatter = locale.dates.getFormatter('time', length=size)
    return formatter.parse(time)


def time_formatter(request, time, size='short'):
    language = ILanguage(request, None)
    locale = locales.getLocale(language=language)
    formatter = locale.dates.getFormatter('time', length=size)
    return formatter.format(time)


def sortable_date_format(date, tz=PARIS, fmt=DATETIME_SHORT):
    """
    @date : the date object, naive or not.

    @tz : the target timezone object.

    @fmt : the wanted output format. Should be a formatting string, same
    as used with `strftime`. Default is a shortened output.
    """
    if isinstance(date, datetime.datetime):
        try:
            return date.astimezone(tz).strftime(fmt)
        except ValueError:
            tzed = date.replace(tzinfo=tz)
            return tzed.astimezone(tz).strftime(fmt)
    elif isinstance(date, datetime.date):
        try:
            return date.strftime(fmt)
        except ValueError:
            tzed = date.replace(tzinfo=tz)
            return tzed.astimezone(tz).strftime(fmt)
    return None


__all__ = ['DATETIME_SHORT', 'format_from_locale', 'date_formatter',
           'date_localizer', 'sortable_date_format']
