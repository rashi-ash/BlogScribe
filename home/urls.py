from django.urls import path
from . import views
# from .views import index,index2

urlpatterns = [    
    path('', views.index, name='index'),
    # path('<int:id>', view.index2, name='index2'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('login/',views.login, name='login'),
    path('logout/',views.logoutview, name='logout'),
    path('blog/<int:id>', views.blog, name='blog'),
    path('blog/delete/<int:id>', views.blog_delete, name='blog-delete'),
    path('blogs', views.blogs, name='blogs')
]
