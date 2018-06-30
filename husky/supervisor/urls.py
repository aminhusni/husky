from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'supervisor'
urlpatterns = [
    path('', views.index, name='index'),
    path('authenticate.html', views.authenticate, name='authenticate'),
    path('checklist.html', views.checklist, name='checklist'),
    path('error.html', views.error, name='error'),
    path('checklist_submit.html', views.checklist_submit, name='checklist_submit'),
    path('supervisor_index.html', views.supervisor_index, name='supervisor_index'),
    path('checklist_report.html', views.checklist_report, name='checklist_report'),
    path('checklist_report_location.html', views.checklist_report_location, name='checklist_report_location'),
    path('performance_report_location.html', views.performance_report_location, name='performance_report_location'),
    path('performance_report.html', views.performance_report, name='performance_report'),
]