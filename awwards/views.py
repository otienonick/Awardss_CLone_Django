from django.shortcuts import redirect, render
from . models import Profile,Post,Like
from .forms  import ProfileModelForm,PostModelForm


# Create your views here.
def my_profile_view(request):
    profile = Profile.objects.get(user = request.user)
    posts = Post.objects.filter(author=request.user).order_by('-created')
    form = ProfileModelForm(request.POST or None ,request.FILES or None,instance = profile)
    p_form = PostModelForm(request.POST or None,request.FILES or None)

    comfirm = False
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            comfirm = True

            
    if p_form.is_valid():
        instance = p_form.save(commit=False)
        instance.author = request.user
        instance.save()
        return redirect('home')
    p_form = PostModelForm()            
         
    context = {
        'profile':profile,
        'form':form,
        'comfirm':comfirm,
        'posts':posts,
        'p_form':p_form,


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

def reviewPhoto(request,pk):
    post = Post.objects.get(id = pk)
    context = {
        'post':post

    }


    return render(request,'awwards/review.html',context)

def like(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id = post_id)
        profile = Profile.objects.get(user = user)
        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)
        like,created = Like.objects.get_or_create(user = profile,post_id = post_id)
        if not created:
            if like.value == 'Like':
                like.value='Unlike'
            else:
                like.value ='Like'   
        else:
            like.value = 'Like'     

            post_obj.save()
            like.save()
            
      
    return redirect('review',pk = post_id )