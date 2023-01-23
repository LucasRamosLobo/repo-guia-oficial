from django.shortcuts import render

# Create your views here.
def home(request):

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
        
    return render(request, "parceiro.html", context)