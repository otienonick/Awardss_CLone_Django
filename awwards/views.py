from django.shortcuts import render
from . models import Profile
from .forms  import ProfileModelForm


# Create your views here.
def my_profile_view(request):
    profile = Profile.objects.get(user = request.user)
    form = ProfileModelForm(request.POST or None ,request.FILES or None,instance = profile)
    comfirm = False
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            comfirm = True
        form = ProfileModelForm()   
         
    context = {
        'profile':profile,
        'form':form,
        'comfirm':comfirm,

    }
    return render(request,'profiles/myprofile.html',context)

def home(request):

    context = {
    }    
    return render(request,'awwards/home.html',context)
