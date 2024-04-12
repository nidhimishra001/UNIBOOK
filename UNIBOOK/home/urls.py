from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('',views.index,name="Home"),
    path('contact',views.contact,name="contact"),
    path('book',views.Book,name="Book"),
    # path('bookform',views.bookform,name="bookform"),
    # path('tagform',views.tagform,name="tagform"),
    path('about',views.about,name="about"),
    path('tag',views.tag,name="tag"),
    path('bookpost/<int:idd>',views.bookpost,name="bookpost"),

    
]