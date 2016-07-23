from datetime import datetime, timedelta
from django.contrib.sessions.models import Session
from polls.models import Visitor, User
from datetime import datetime
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import auth
class UserRestrictMiddleware(object):
    """
    Prevents more than one user logging in at once from two different IPs
    """

    def process_request(self, request):

        if not request.user.is_authenticated():
            # Can't log out if not logged in
            return
        if isinstance(request.user, User):
            current_key = request.session.session_key
            if hasattr(request.user, 'visitor'):
                active_key = request.user.visitor.session_key
                print active_key, current_key
                if active_key != current_key:
                    return HttpResponseRedirect(reverse('polls:no_multisession'))
            else:
                Visitor.objects.create(
                    pupil=request.user,
                    session_key=current_key,
                )
        try:
            if datetime.now() - request.session['last_touch'] > timedelta(0, settings.AUTO_LOGOUT_DELAY * 60, 0):
                auth.logout(request)
                del request.session['last_touch']
                return
        except KeyError:
            pass

        request.session['last_touch'] = datetime.now()