from rest_framework import serializers
from awwards.models import Post,Profile

        

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','project_name','description','url','image','location','author','created','liked']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','username','bio','avatar','user','created']
