from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'feedback'
urlpatterns = [
    path('', views.index, name='index'),
    path('setup.html', views.setup, name='setup'),
    path('setlocation.html', views.setlocation, name='setlocation'),
    path('rating_submit.html', views.rating_submit, name='rating_submit'),
    path('problem.html', views.problem, name='problem'),
    path('problem_submit.html', views.problem_submit, name='problem_submit'),
    path('thankyou.html', views.thankyou, name='thankyou'),

    
]