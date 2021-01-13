from django import forms
from django.shortcuts import render,HttpResponse

# Create your views here.
people = []   #people
accounts = dict()

#FORM for template.

class NewEntryForm(forms.Form):

    name = forms.CharField(label = "Name",max_length=40)
    debit = forms.IntegerField(label = "Taken")
    credit = forms.IntegerField(label="Given")
    date = forms.DateField(label="On")



def home(request):
    return render(request,"home/home.html")

def showAll(request):
    return render(request, "home/showall.html", context={
        "people":people
    })
def add(request):
    if request.method == 'POST':
        form = NewEntryForm(request.POST)
        if form.is_valid():
            person = form.cleaned_data['name']
            s = [form.cleaned_data['debit'],form.cleaned_data['credit'],form.cleaned_data['date']]
            people.append(person)
            try:
                accounts[person].append(s)
            except Exception:
                accounts[person] = [s]
        else:
            return render(request,"home/add.html", {
                "form":form
            })

    return render(request, "home/add.html",
    {
        "form":NewEntryForm()
    })

def showPerson(request):
    pass