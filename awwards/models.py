from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length = 255,blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(default='no bio...',max_length=300)
    avatar = models.ImageField(default='avatar.png',upload_to = 'avatars/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}-{self.created}'

class Post(models.Model):
    project_name = models.CharField(max_length = 255)
    description = models.TextField()
    url = models.URLField(unique=True)
    image = models.ImageField(upload_to = 'posts',validators = [FileExtensionValidator(['png','jpg','jpeg'])])
    liked = models.ManyToManyField(Profile,blank =True,related_name='likes')
    location = models.CharField(max_length = 255)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')

    # number of likes
    def get_likes(self):
        return self.liked.all().count()   

    def __str__(self):
        return str(self.description[:20])

    def save_project(self):
        self.save() 

    def delete_project(self):
        self.delete()  

    def  update_project(self):
        self.save()  

    @classmethod
    def get_project_by_id(cls,id=None):
        photos = cls.objects.filter(id = id)   
        return photos     
        
    @classmethod
    def search_by_project_name(cls,search_term):
        project = cls.objects.filter(project_name__icontains = search_term)   
        # We filter the model data using the __icontains query filter
        return project     

    class Meta:
        ordering = ['-created'] 

LIKE_CHOICES =(
    ('Like','Like'),
    ('Unlike','Unlike')
)


class Like(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)     
    post = models.ForeignKey(Post,on_delete=models.CASCADE)  
    value = models.CharField(choices=LIKE_CHOICES,max_length=8)   
  

    def __str__(self):
        return f'{self.user}-{self.post}-{self.value}'

