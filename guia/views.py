from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .models import Local
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.urls import reverse_lazy





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
    if request.method=="POST":
        wpp=request.POST['wpp']
        email=request.POST['email']
        email_form=settings.EMAIL_HOST_USER
        recipient_list=["lucasramoslobo83@gmail.com"]
        send_mail('Contato guia sul da bahia','email: ' + email + '  wpp: ' + wpp, email_form, recipient_list)
        return redirect('/guia-sul-da-bahia/')
    context = {
        "title":"sobre",
      
    }  
        
    return render(request, "about.html", context)

def parceiro(request):
    if request.method=="POST":
        wpp=request.POST['wpp']
        email=request.POST['email']
        email_form=settings.EMAIL_HOST_USER
        recipient_list=["lucasramoslobo83@gmail.com"]
        send_mail('Contato guia sul da bahia','email: ' + email + '  wpp: ' + wpp, email_form, recipient_list)
        return redirect('/parceiro-guia-sul-da-bahia/')
    context = {
        "title":"parceiro",
      
    }  
        
    return render(request, "pricing.html", context)

def search(request, *args, **kwargs):
    recipes = Local.objects.all()
    inter = []
    results1=[]
    results2=[]
    results3=[]
    results4=[]
    results5=[]
    results6=[]
    results7=[]
    results8=[]
    results9=[]
    results10=[]
    results=[]
    b = False

    if "search" in request.GET:
        query = request.GET.get("search")
        queryset = recipes.filter(Q(Nome__icontains=query))
        results = recipes.filter(Q(Nome__icontains=query))
        topic = ''
        cidade =''

    if request.GET.get("Itacaré"):
        results1 = queryset.filter(Q(Cidade__Nome__icontains="Itacaré"))
        cidade = "Itacaré"
        b = True
    if request.GET.get("Ilhéus"):
        results2 = queryset.filter(Q(Cidade__Nome__icontains="Ilhéus"))
        cidade="Ilhéus"
        b = True    
 
    if request.GET.get("Passeios"):
        results3 = queryset.filter(Q(Categoria__Nome__icontains="Passeios"))
        topic = "Passeios"
        b = True  
    if request.GET.get("Restaurantes"):
        results4 = queryset.filter(Q(Categoria__Nome__icontains="Restaurantes"))
        topic="Restaurantes"
        b = True 
    if request.GET.get("Transfers"):
        results5 = queryset.filter(Q(Categoria__Nome__icontains="Transfers"))
        topic="Transfers"
        b = True 
    if request.GET.get("Hospedagens"):
        results6 = queryset.filter(Q(Categoria__Nome__icontains="Hospedagens"))
        topic="Hospedagens"
        b = True 
    if request.GET.get("Esportes"):
        results7 = queryset.filter(Q(Categoria__Nome__icontains="Esportes"))
        topic="Esportes"
        b = True 

    if request.GET.get("Experiências"):
        results8 = queryset.filter(Q(Categoria__Nome__icontains="Experiências"))
        topic="Experiências"
        b = True 
    
    a = False
    for x in recipes:
        for y in results3:
            if x == y:
                if x not in inter:
                    inter.append(x)
                    a = True
        for y in results4:
            if x == y:
               if x not in inter:
                    inter.append(x)
                    a = True
        for y in results5:
            if x == y:
               if x not in inter:
                    inter.append(x)
                    a = True
        for y in results6:
            if x == y:
                if x not in inter:
                    inter.append(x)
                    a = True
        for y in results7:
            if x == y:
               if x not in inter:
                    inter.append(x)
                    a = True
        for y in results8:
            if x == y:
               if x not in inter:
                    inter.append(x)
                    a = True
        for y in results9:
            if x == y:
                if x not in inter:
                    inter.append(x)
                    a = True
        for y in results10:
            if x == y:
               if x not in inter:
                    inter.append(x)
                    a = True
          
    if a == False and b == False:
        inter = results
                
    
    #paginate results
    paginator = Paginator(results, 3)
    page = request.GET.get("page")
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)

    context = {
        "cidade":cidade,
        "topic":topic,
        "page":page,
        "results2":results2,
        "results3":results3,
        "results4":results4,
        "results5":results5,
        "results6":results6,
        "results7":results7,
        "results8":results8,
        "results9":results9,
        "results10":results10,
        "query":query,
        "results":results,
        "results1":results1,
        "inter":inter,
   
       
    }
    return render(request, "search.html", context)

def detail(request, slug, *args, **kwargs):
    recipe = get_object_or_404(Local, slug=slug)
    context = {
        "recipe":recipe,
        "cidade":recipe.Cidade,
    }
    return render(request, "detail.html", context)

