# my created
# render takes three inputs request,filename,variable

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    
    return render(request,"index.html")
    # return HttpResponse("HOME")

def analize(request):
    
    dtext=request.POST.get("text","default")
    removepunc=request.POST.get("removepunc","off")
    uppercase=request.POST.get("capital","off")
    removespace=request.POST.get("spaceremover","off")
    charcount=request.POST.get("charcount","off")

    if removepunc=="on":

        punctuation=""" ! " $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ { | } ~"""
        analizedt=""
        for char in dtext:
            if char not in punctuation:
                analizedt=analizedt+char
        
        v={"purpose":"Punctuation Removed","analyxet_text":analizedt}

        return render(request,"analized.html",v)
    
    elif uppercase=="on":
        analizedt=dtext.upper()
        v={"purpose":"UPPER CASE","analyxet_text":analizedt}

        return render(request,"analized.html",v)
    
    elif removespace=="on":

        analizedt=dtext.replace("  "," ")
        v={"purpose":"SPACE REMOVE","analyxet_text":analizedt}

        return render(request,"analized.html",v)
    
    elif charcount=="on":
        
        analisedt=str(len(dtext))
        
        v= {"purpose":"CHARACTER COUNT","analyxet_text":analisedt}

        return render(request,"analized.html",v)
     
    else:
        HttpResponse("Error")