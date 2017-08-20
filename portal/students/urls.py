from django.conf.urls import url

from . import views
app_name = 'students'
urlpatterns = [
    # ex: /polls/
    # url(r'^$', views.StudentList.as_view(), name='student_list'),
    # url(r'^create/$', views.StudentCreate.as_view(), name='student_create'),
    # url(r'^edit/(?P<pk>\d+)$', views.StudentUpdate.as_view(), name='student_edit'),
    # url(r'^delete/(?P<pk>\d+)$', views.StudentDelete.as_view(), name='student_delete'),

    url(r'^$', views.student_list, name='student_list'),
    url(r'^create/$', views.student_create, name='student_create'),
    url(r'^edit/(?P<pk>\d+)$', views.student_edit, name='student_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.student_delete, name='student_delete'),

]