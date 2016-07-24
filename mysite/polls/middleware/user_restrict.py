from datetime import datetime, timedelta
from django.contrib.sessions.models import Session
from polls.models import Visitor, User

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

class UserRestrictMiddleware(object):
    """
    Prevents more than one user logging in at once from two different IPs
    """

    def process_request(self, request):
        print "here in UserRestrict Middleware"
        if request.path == reverse('admin:index'):
            print "requesting admin page"
            return
        #if (request.user.is_active and request.user.is_superuser):
        #    print "user is a super user"
        #    return
        if isinstance(request.user, User):
            current_key = request.session.session_key
            if hasattr(request.user, 'visitor'):
                active_key = request.user.visitor.session_key
                print active_key, current_key
                if active_key != current_key:
                    print "user already logged in!!"
                    Session.objects.get(session_key=current_key).delete()
                    return HttpResponseRedirect(reverse('polls:no_multisession'))
            else:
                print "creating user object"
                visitor = Visitor.objects.create(
                    pupil=request.user,
                    session_key=current_key,
                )
                visitor.save()




