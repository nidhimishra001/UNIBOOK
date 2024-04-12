from ctypes.wintypes import HACCEL
from django.shortcuts import render 
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse
# from httplib2 import Http
from home.models import  Contact,Book,Tag 
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from home.forms import ContactForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import json


# Create your views here.
def index(request):
    
    if(request.user.is_anonymous):
        return redirect("/login")
    else:
        if(request.GET.get('tag')!=None):
            tag=request.GET.get('tag', 1)
            blog=Book.objects.filter(tags__in=[tag])
        else:
            
            blog=Book.objects.all()   
                #pagination
        page=request.GET.get('page',1)
        paginator=Paginator(blog,3)
        try:
            blog=paginator.page(page)
        except PageNotAnInteger:
            blog=paginator.page(1)
        except EmptyPage:
            blog=paginator.page(paginator.num_pages)


        context={
            
            'blogs':blog,
              }

        return render(request,'index.html',context)

def contact(request):
    if(request.user.is_anonymous):
        return redirect("/")
    else:
        if(request.method=="POST"):
            form=ContactForm()  
            if form.is_valid():
                form.save(request.POST)
                messages.add_message(request, messages.INFO, 'success')

            

        else:
            form = ContactForm()  

            context={'form':form}    

            return render(request,'contact.html',context)        
    

# def contact(request):
#     if(request.user.is_anonymous):
#         return redirect("/login")
#     else:
#         if (request.method=='POST'):
#                 name=request.POST['name']
#                 email=request.POST['email']
#                 phone=request.POST['phone']
#                 description=request.POST['description']
#                 contact=Contact(name=name,phone=phone,email=email,description=description)
#                 contact.save()  
#         return render(request,'contact.html')  

def loginUser(request):
     if(request.method=="POST"):
         username=request.POST['username']
         password=request.POST['password']

         user=authenticate(username=username,password=password)
         if user is not None:
            login(request,user)
            return redirect("/")

         else:
              return render(request,'login.html')
     return render(request,'login.html')

def logoutUser(request):
     logout(request)
     return redirect('/login')

def blogpost(request,idd):
    # if(request.user.is_anonymous):
    #     return redirect("/login")
    # else:
        blogpost=Book.objects.get(id=idd)
        # contact.name="Test"
        # contact.save()
        context={
                'blogpost':blogpost
            } 
        # return render(request,'contact.html') 
        return render(request,'blogpost.html',context)  
def books(request):
    if(request.user.is_anonymous):
        return redirect('/login')
    else:
        books=Book.objects.all()
        
        context={
                'books':books
            } 
        
        return render(request,'books.html',context) 



def bookpost(request,idd):
    if(request.user.is_anonymous):
        return redirect("/login")
    else:
        blogpost=Book.objects.get(id=idd)
        
        context={
                'bookpost':bookpost
            } 
        
        return render(request,'blogpost.html',context) 



def tag(request):
    if (request.method=='POST'):
        Title=request.POST['Title'] 
        tag =Tag(Title=Title)  
        tag.save()
    return render(request,'tag.html') 

def about(request):
    if(request.user.is_anonymous):
        return redirect('/login') 
    return render(request,'about.html')         


def blogpostupdate(request,idd):
    if(request.user.is_anonymous):
        return redirect('/login')
    else:
        blogs=Book.objects.get(id=idd)
        form=BlogFrom(initial={'userid':request.user.id,'username':request.user.username,'title':blogs.title,'description':blogs.description,'image':blogs.image,'date':blogs.date,'tags':blogs.tags.all})
        if(request.method == 'POST'):
            # request.POST['user_id']=request.user.id
            form=BlogFrom(request.POST,request.FILES,instance=blogs)
            # form.data['user_id']=request.user.id
            print("filed form",form['userid'].value())
            form.errors.as_data()
            if(form.is_valid()):
                print("validated")
                form.save()
                messages.add_message(request, messages.INFO, 'success')
            else:
                print("error")
                errors=form.errors.as_json()
                print(errors)
                # errors = json.loads(errors)
                # message=errors["userid"]
                # message = json.loads(message)
                # print(message)
                
                messages.add_message(request, messages.INFO, 'failed')
        
        
        context={
                'form':form,
                'id':idd
            }
        return render(request, 'blogupdate.html',context)


def blogpostdelete(request,idd):
    blogs=Book.objects.get(id=idd)
    blogs.delete()
    return redirect("/index")
def about(request):
    return HttpResponse("This is an about page")

    

def blogform(request):
    if(request.user.is_anonymous):
        return redirect('/login')
    else:
        form=BlogFrom(initial={'userid':request.user.id,'username':request.user.username})
        if(request.method == 'POST'):
            # request.POST['user_id']=request.user.id
            form=BlogFrom(request.POST,request.FILES)
            # form.data['user_id']=request.user.id
            print("filed form",form['userid'].value())
            form.errors.as_data()
            if(form.is_valid()):
                print("validated")
                form.save()
                messages.add_message(request, messages.INFO, 'success')
            else:
                
                errors=form.errors.as_json()
                
                messages.add_message(request, messages.INFO, 'failed')
        
        
        context={
                'form':form
            }
        return render(request,'blogform.html',context)
              
           
