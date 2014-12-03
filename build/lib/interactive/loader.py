from django.conf import settings
import imp

class Loader(object):

    def load(self):
        for app in settings.INSTALLED_APPS:
            try:
                __import__(app + '.views')
            except Exception, e:
                pass
