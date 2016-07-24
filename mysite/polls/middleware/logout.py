class Logout(object):
    def process_request(self, request):
        visitor = Visitor.objects.filter(pupil=request.user)
        print "In logout middleware deleting visitor object for {0}".format(visitor)
        if visitor:
            visitor.delete()