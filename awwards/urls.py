from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from .views import my_profile_view,home,reviewPhoto,like,search_results,delete_project,update_project

urlpatterns = [
    path('myprofile/',my_profile_view,name ='profile'),
    path('' , home , name='home'),
    path('reviewPost/<str:pk>' , reviewPhoto , name='review'),
    path('like/',like, name = 'like'),
    path('search/',search_results, name ='search_results'),
    path('delete/<int:pk>',delete_project, name = 'deletepost'), 
    path('update/<str:pk>',update_project, name = 'updatepost'), 



]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)