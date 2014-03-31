# -*- coding: utf-8 -*-

import datetime
import pytz

from zope.i18n.locales import LocaleFormat
from zope.i18n.interfaces.locales import ILocale
from zope.i18n.format import DateTimeFormat


BASE = pytz.utc
PARIS = pytz.timezone('Europe/Paris')
DATETIME_SHORT = '%Y-%m-%d %H:%M'


# This needs proper registration
# And localization.
base_format = LocaleFormat()
base_format.pattern = u'dd/MM/yyyy'


def format_from_locale(locale, date, tz=PARIS, fmt='dateTime', size='medium'):
    """
    @locale : a valid `ILocale` object. See ``zope.i18n`` for
    more information.

    @date : the date object, naive or not.

    @tz : the target timezone object.

    @fmt : the wanted output format. Should be a 'formatter' name.
    see zope.i18n date localizer for more information.
    """
    if (isinstance(date, datetime.date) and
        not isinstance(date, datetime.datetime)):
        date = datetime.datetime.combine(date, datetime.time())
    if date is not None and isinstance(date, datetime.datetime):
        formatter = locale.dates.getFormatter(fmt, size)
        try:
            return formatter.format(date.astimezone(tz))
        except ValueError:
            tzed = date.replace(tzinfo=BASE)
            return formatter.format(tzed.astimezone(tz))
    return None


def date_localizer(request, date, tz=PARIS, fmt='dateTime', size='medium'):
    locale = ILocale(request)
    return format_from_locale(locale, date, tz, fmt, size)


def date_formatter(request, date, formatter=base_format):
    # This needs a lot more work.
    locale = ILocale(request)
    calendar = locale.dates.calendars.get('gregorian')
    return DateTimeFormat(formatter.pattern, calendar).format(date)


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
