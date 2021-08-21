from django.urls import path
from . import views


app_name = 'website'


urlpatterns = [
    path('', views.home, name='home'),
    # path(views.home1, name='home1'),
    # path('', views.contact, name='contact'),
    path('send_gmail/', views.send_gmail, name='send_gmail'),
    # path('send_mail/', send_gmail, name="send_mail"),
]