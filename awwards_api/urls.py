from django.urls import path


from .views import PostList,Overview,SinglePost,UserProfileViewSet


snippet_list = UserProfileViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

snippet_detail = UserProfileViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
urlpatterns = [
    path('posts',PostList.as_view()),
    path('',Overview.as_view()),
    path('posts/<int:pk>',SinglePost.as_view()),
    path('profile/',snippet_list),
    path('profile/<int:pk>/', snippet_detail),


# AUTHENTICATION

 
]