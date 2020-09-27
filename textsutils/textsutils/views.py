#I have created this file--SAIF
from django.http import  HttpResponse
from django.shortcuts import render
def index(request):
    #params={"name":"saif","place":"Mars"}
    #return  render(request,'index.html',params#
    return render(request,'index1.html')
    #return HttpResponse("hello SAIF")
def about(request):
    return HttpResponse("<h1>About hello SAIF </h1>")
def facebook(request):
    return HttpResponse("""<a href="https://www.facebook.com/"> FACEBOOK</a>""")
def youtube(request):
    return HttpResponse("""<a href="https://www.youtube.com/"> YOUTUBE</a>""")
def linkedin(request):
    return HttpResponse("""<a href="https://www.linkedin.com/feed/"> LINKEDIN</a>""")
def naukri(request):
    return HttpResponse("""<a href="https://www.naukri.com/mnjuser/homepage"> NAUKRI</a>""")
def instagram(request):
    return HttpResponse("""<a href="https://www.instagram.com/"> INSTAGRAM</a>""")
def removepunc(request):
    djtext=request.GET.get('text','default')
    print(djtext)
    return  HttpResponse("""remove punc </br>
    <a href="http://127.0.0.1:8000/"> home</a>""")
def newlineremove(request):
    return  HttpResponse(" new line remove")
def capfirst(request):
    return  HttpResponse("capitalize first")
def spaceremove(request):
    return  HttpResponse("space remover")
def charcount(request):
    return  HttpResponse("char count")
def analyze(request):
    djtext=request.GET.get('text','default')
    analyzed=djtext
    params={'purpose':'Removing Punctuations', 'analyzed_text':analyzed}
    return render(request,'analyze.html',params)


