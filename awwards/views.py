from django.shortcuts import render
from . models import Profile,Post
from .forms  import ProfileModelForm


# Create your views here.
def my_profile_view(request):
    profile = Profile.objects.get(user = request.user)
    posts = Post.objects.filter(author=request.user).order_by('-created')
    form = ProfileModelForm(request.POST or None ,request.FILES or None,instance = profile)
    comfirm = False
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            comfirm = True
         
    context = {
        'profile':profile,
        'form':form,
        'comfirm':comfirm,
        'posts':posts

    }
    return render(request,'profiles/myprofile.html',context)

def home(request):
    posts = Post.objects.all()
    profile = Profile.objects.get(user =request.user)
    context = {
        'posts':posts,
        'profile':profile,
    }

    return render(request,'awwards/home.html',context)
