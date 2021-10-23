from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from awwards.models import  Post, Profile
from .serializers import PostSerializer,ProfileSerializer
from rest_framework import   status,viewsets
from .permissions import IsAdminOrReadOnly


class Overview(APIView):
    def get(self,request):

        api_urls = {
            'get-all-posts': '/posts',
            'create a post':'/posts',
            'get-single-post':'/posts/<int:id>',
            'update-post':'/posts/<int:id>',
            'delete-posts':'/posts/<int:id>',
            'profiles':'/profile',
            'get-single-profile':'/profile/<int:id>',
            'update-profile':'/profile/<int:id>',
            'delete-profile':'/profile/<int:id>',

        }

        return Response(api_urls)
class PostList(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):
        all_merch = Post.objects.all()
        serializers = PostSerializer(all_merch, many=True)
        return Response(serializers.data)   

    def post(self, request, format=None):
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)    

class SinglePost(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request,pk,format=None):
        serializers = Post.objects.get(id = pk)  
        serializer = PostSerializer(serializers, many=False)
        return Response(serializer.data)
        
    def delete(self,request,pk,format=None):
        serializers = Post.objects.get(id = pk)  
        serializers.delete()
        return Response("merchandise successfully deleted!")  
        
    def put(self, request, pk, format=None):
        serializers = Post.objects.get(id = pk)  
        serializer = PostSerializer(serializers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

class UserProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()




