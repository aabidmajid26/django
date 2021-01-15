from django import forms
from django.shortcuts import render,HttpResponse
from django.urls import reverse
from django.contrib.admin import widgets
import datetime

# Create your views here.
# people = dict()   #people
# accounts = dict()

#FORM for template.


class NewEntryForm(forms.Form):

    name = forms.CharField(label = "Name",max_length=40)
    debit = forms.IntegerField(label = "Taken", initial=0,min_value=0)
    credit = forms.IntegerField(label="Given",initial=0,min_value=0)
    date = forms.DateField(
        label="On ", 
        initial=datetime.date.today,
        widget=forms.widgets.DateInput(attrs={'type':'date'}))



def home(request):
    request.session.modified = True
    if "people" not in request.session:
        request.session['people'] = dict({'hello':1})
    if "accounts" not in request.session:
        request.session['accounts'] = dict({'hello':[[12,12,2020-20-20]]})
    return render(request,"home/home.html")

def showAll(request):
    return render(request, "home/showall.html", context={
        "people":request.session['people']
    })
def add(request):
    if request.method == 'POST':
        form = NewEntryForm(request.POST)
        if form.is_valid():
            person = form.cleaned_data['name']
            s = [form.cleaned_data['debit'],form.cleaned_data['credit'],form.cleaned_data['date']]
            request.session['people'][person]=1
            try:
                request.session['accounts'][person]+=[s]
                print('appended to accounts[',person,']')
            except Exception:
                request.session['accounts'][person] = [s]
                print('added to accounts[',person,']')
        else:
            return render(request,"home/add.html",{"form":form})
    return render(request, "home/add.html",{"form":NewEntryForm()})





# def add(request):
#     if request.method == 'POST':
#         form = NewEntryForm(request.POST)
#         if form.is_valid():
#             person = form.cleaned_data['name']
#             s = [form.cleaned_data['debit'],form.cleaned_data['credit'],form.cleaned_data['date']]
#             people[person]=1
#             try:
#                 accounts[person].append(s)
#                 print(s,'appended to', person)
#                 print(accounts)
#             except Exception:
#                 accounts[person] = [s]
#                 print(s,'added to ', person)
#                 print(accounts)
#         else:
#             return render(request,"home/add.html", {
#                 "form":form
#             })

#     return render(request, "home/add.html",
#     {
#         "form":NewEntryForm()
#     })

def showPerson(request,name):
    print(request.session['accounts'])
    try:
        return render(request, "home/person.html",{
            "record":request.session['accounts'][name],
            "exists":True,
            "name":name
        })
    except KeyError:

        print('keyerror')
        return render(request, "home/person.html",{
            "name":name,
            "exists":False
        })