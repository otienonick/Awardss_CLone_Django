from django.shortcuts import redirect, render
from . models import Profile,Post,Like
from .forms  import ProfileModelForm,PostModelForm
from django.contrib.auth.decorators import login_required
import datetime as dt



# Create your views here.
# @login_required(login_url='/accounts/login/')

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
    date = dt.date.today()

    context = {
        'posts':posts,
        'date':date
    }

    return render(request,'awwards/home.html',context)

@login_required(login_url='/accounts/login/')
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

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_articles = Post.search_by_project_name(search_term)
        message = f"{search_term}"
        context = {"message":message,
        "projects": searched_articles}

        return render(request, 'awwards/search.html',context)
    else:
        message = "no projects found"
        context = {
            'message':message
        }
        return render(request, 'awwards/home.html',context)  

def delete_project(request,pk): 
    post = Post.objects.get(pk = pk)
    if request.method == 'POST':
        post.delete()

        return redirect('home')

    return render(request, 'awwards/delete_project.html',{})        


def update_project(request,pk):
    post = Post.objects.get(id = pk)
    form = PostModelForm(instance = post)
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES ,instance = post)
        # We pass in the request.FILES argument because we are going to be uploading an Image file and we want to process that in our form.
        if form.is_valid():
            post.save()
            return redirect('review',pk = pk )
   
    return render(request, 'awwards/update_project.html',{'form' :form})