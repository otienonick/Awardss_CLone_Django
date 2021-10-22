from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from .views import my_profile_view,home

urlpatterns = [
    path('myprofile/',my_profile_view,name ='profile'),
    path('' , home , name='home'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)