import inflect
import pytz
from datetime import datetime
from datetime import timedelta

from payslipsproject.settings import ACTUAL_BASE_PATH

__author__ = 'oliverqueen'


from django.template import Library
import platform

register = Library()

@register.filter(name="getStaticPath")
def get_static_path(url):
    physical_path = ACTUAL_BASE_PATH + url
    physical_path = physical_path.replace("\\", "/")
    return physical_path

@register.filter(name="getPaySlipDate")
def get_pay_slip_date(value):
    today_date = datetime.now().date().strftime('%B, %Y')
    return today_date

@register.filter(name="getValue")
def get_key_value_from_dict(input_dict, key):
    return input_dict.get(key, "Not Provided")

@register.filter(name="convertToWords")
def convert_to_words(currency_value):
    inflect_config = inflect.engine()
    to_words = inflect_config.number_to_words(currency_value)
    return to_words + "-rupees-only"

@register.filter(name='convertTimeToLocal')
def convert_utc_to_local_time(utc_time):
    return utc_time + timedelta(hours=5, minutes=30)