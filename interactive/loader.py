"""
This modle dynamically loads the registered 
views and keeps a dictionary of them.

Other classes can access this dictionary.

"""
from django.conf import settings
import imp

class Loader(object):

    def load(self):
        for app in settings.INSTALLED_APPS:
            try:
                __import__(app + '.views')
            except Exception, e:
                pass
