from payslipsproject.settings import ACTUAL_BASE_PATH

__author__ = 'oliverqueen'


from django.template import Library

register = Library()

@register.filter(name="getStaticPath")
def get_static_path(url):
    physical_path = ACTUAL_BASE_PATH + url
    physical_path = physical_path.replace("\\", "/")
    return physical_path