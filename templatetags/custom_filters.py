__author__ = 'oliverqueen'

from django.template import Library

register = Library()

register.filter(name="getStaticPath")
def get_static_path(url):
    print url
    return ""