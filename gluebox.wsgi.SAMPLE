import os
import sys

path = '/home/user/public'
if path not in sys.path:
    sys.path.append( path )
    sys.path.append(os.path.join( path, "gluebox" ) )

os.environ['DJANGO_SETTINGS_MODULE'] = 'gluebox.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
