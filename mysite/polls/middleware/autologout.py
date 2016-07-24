from datetime import datetime, timedelta
from django.conf import settings
from django.contrib import auth
from polls.models import Visitor, User
class AutoLogout(object):
    def process_request(self, request):
        if not request.user.is_authenticated():
            # Can't log out if not logged in
            print "user not logged in {0}".format(request.user)
            return
        try:
            if datetime.now() - request.session['last_touch'] > timedelta(0, settings.AUTO_LOGOUT_DELAY * 60, 0):
                visitor = Visitor.objects.filter(pupil=request.user)
                print "deleting visitor object for {0}".format(visitor)
                if visitor:
                    visitor.delete()
                auth.logout(request)
                del request.session['last_touch']
                return
        except KeyError:
            pass
        request.session['last_touch'] = datetime.now()