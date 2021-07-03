from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    works = recentProject.objects.all()
    context = {'works':works,}
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        messages = request.POST['msg']
        msg= message(firstName=firstname,lastname=lastname,email=email,message=messages)
        msg.save()
    return render(request,"index.html",context)


def msg(request):#to see messages
    messages = message.objects.all()
    context={
        'title':"messages",
        'messages':messages,
    }
    return render(request,'message.html',context)

def delete(request,m_id):
    message.objects.get(pk=m_id).delete()
    messages = message.objects.all()
    context={
        'title':"messages",
        'messages':messages,
    }
    return render(request,'message.html',context)
