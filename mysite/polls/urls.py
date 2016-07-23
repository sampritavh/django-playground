from django.conf.urls import url

from . import views
app_name = 'polls'

urlpatterns = [
    url(r'^q/$', views.QuestionListView.as_view(), name='questions'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^$', views.loginView, name='index'),
    url(r'^login/$',views.process_login, name='login'),
    url(r'^logout/$',views.logout_view, name='logout'),
    url(r'^sessionerror/$',views.no_multisession, name='no_multisession'),
]