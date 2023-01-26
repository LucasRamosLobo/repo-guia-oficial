from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    if request.method=="POST":
        wpp=request.POST['wpp']
        email=request.POST['email']
        email_form=settings.EMAIL_HOST_USER
        recipient_list=["lucasramoslobo83@gmail.com"]
        send_mail('Contato guia sul da bahia','email: ' + email + '  wpp: ' + wpp, email_form, recipient_list)
        return redirect('/')
    context = {
        "title":"home",
      
    }  
        
    return render(request, "index.html", context)

def sobre(request):

    context = {
        "title":"sobre",
      
    }  
        
    return render(request, "about.html", context)

def parceiro(request):

    context = {
        "title":"parceiro",
      
    }  
        
    return render(request, "pricing.html", context)