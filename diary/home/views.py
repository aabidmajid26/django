from django.shortcuts import render,HttpResponse

# Create your views here.
people = ['Hello', 'World', 'Karma', 'Jarma']   #people
accounts = [] #2d list.
def home(request):
    return render(request,"home/home.html")

def showAll(request):
    return render(request, "home/showall.html", context={
        "people":people
    })