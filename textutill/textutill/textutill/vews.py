# i havecriate this file akshay
from importlib.resources import contents
import re
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render
from requests import request

def index(request):
    return render(request,'indexx.html')
    # return HttpResponse("Home")

def analyse(request):
    # get the text 
    djtext=request.POST.get('text','default')
    # check box value
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off') 
    newlineremover=request.POST.get('newlineremover','off') 
    extraspaceremover=request.POST.get('extraspaceremover','off')   
    charactorcounter=request.POST.get('charactorcounter','off')  
    # check which checkbox is on
    if removepunc=="on":
        punctuations= ''':()-[]{};:'"\,<>./?~!@#$%^&*-_'''
        analysed=""
        for char in djtext:
            if char not in punctuations:
                analysed=analysed+char
        params= {'purpose':'removepunctutions','analyse_text':analysed}
        djtext=analysed
        #return render(request,'analyse.html',params)
    if fullcaps=="on":
        analysed=""
        for char in djtext:
            analysed=analysed + char.upper()
        params= {'purpose':'change to upper case','analyse_text':analysed}
        djtext=analysed
        # return render(request,'analyse.html',params)    
    if newlineremover=="on":
        analysed=""
        for char in djtext:
            if char !="\n"and char !="\r":
                analysed=analysed + char
        params= {'purpose':'remove new lines','analyse_text':analysed}
        djtext=analysed
        # return render(request,'analyse.html',params)      
    if extraspaceremover=="on":
        analysed=""
        for index, char in enumerate(djtext):
            if djtext[index] ==" "and djtext[index+1]==" ":
                pass
            else:
                analysed=analysed + char
        params= {'purpose':'remove new lines','analyse_text':analysed}
        djtext=analysed
        # return render(request,'analyse.html',params)                
    
    if charactorcounter =="on":
        analysed=0
        for char in djtext:
            analysed=analysed+1
        params= {'purpose':'remove new lines','analyse_text':analysed}
    if (removepunc!="on"and fullcaps!="on"and newlineremover!="on" and extraspaceremover!="on" and charactorcounter !="on"):
        return HttpResponse("plese select any one operation and try again")
        # return render(request,'analyse.html',params)      
    
    return render(request,'analyse.html',params)       
def phno(request):
    return HttpResponse("6378176772")   
def emailid(request):
    return HttpResponse("akshayshama3@gmail.com")  