from django.shortcuts import render,redirect
from .models import BlogModel, CommentModel
from .form import BlogForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    form = UserCreationForm()
    if request.method == 'POST':
        if 'login' in request.POST:
            print('login')
            username1 = request.POST['user-email']
            password = request.POST['password']
            user = authenticate(request, username=username1, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')
        else:
            print('register')
            print(request.POST)
            form = UserCreationForm(request.POST)
            if form.is_valid():
                print('its Valid')
                form.save()

    return render(request, 'login.html', {
        'form': form
    })

def logoutview(request):
    logout(request)
    return redirect('login')
# def index2(request):
#     return redirect('index2', id=1)

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def blogs(request):
    return render(request,'blogs.html', {
        'blogs': BlogModel.objects.order_by('-updatedtime')
    })


def index(request):
    #   x=BlogModel.objects.all()
      if request.method == 'POST':
        
        if 'create-blog' in request.POST:
            
            BlogModel.objects.create(title=request.POST['title'], desc=request.POST['desc'], image=request.FILES['image'], user=request.user)
        
      
      x=BlogModel.objects.order_by('-updatedtime')[:4]
      return render(request,'index.html',{ 
        'blogModel': x,
        'form': BlogForm()
        }
      )



# def login(request):
#     return render(request,'login.html')
def blog(request, id):
    x = BlogModel.objects.get(id=id)
    if request.method == 'POST':
        message = request.POST['message']
        if message.strip() != "":
                CommentModel.objects.create(message=message, user=request.user, blog=BlogModel.objects.get(id=request.POST['blog'])) 
    return render(request,'blog.html', {
        'data': x,
        'comments': CommentModel.objects.filter(blog=BlogModel.objects.get(id=id))
    })

def blog_delete(request, id):
    BlogModel.objects.get(id=id).delete()
    return redirect('index')

