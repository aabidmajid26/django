from django import forms
from django.shortcuts import render,HttpResponse
from django.urls import reverse
from django.contrib.admin import widgets
import datetime
from django.http import HttpResponseRedirect

from .models import People, Transactions



class NewEntryForm(forms.Form):

    name = forms.CharField(label = "Full Name",max_length=60)
    residence = forms.CharField(label="Residence", max_length=40)
    debit = forms.IntegerField(label = "Taken", initial=0,min_value=0)
    credit = forms.IntegerField(label="Given",initial=0,min_value=0)
    # date = forms.DateField(
    #     label="On ", 
    #     initial=datetime.date.today,
    #     widget=forms.widgets.DateInput(attrs={'type':'date'}))



def home(request):
    return render(request,"home/home.html")

def showAll(request):
    return render(request, "home/showall.html", context={
        "people":People.objects.all()
    })
def add(request):
    if request.method == 'POST':
        form = NewEntryForm(request.POST)
        if form.is_valid():
            person = form.cleaned_data['name']
            rdence = form.cleaned_data['residence']
            dbt,crdt = [form.cleaned_data['debit'],form.cleaned_data['credit']]
            fname,lname = person.split()

            try:
                trans_id = Transactions.objects.last().id+1
            except AttributeError:
                trans_id=1

            try:
                person = People.objects.get(first_name=fname,last_name=lname,residence=rdence)
                p_id = person.id
                
            except Exception:
                p_id = len(People.objects.all())+1
                person = People(p_id, fname,lname,rdence)
                person.save()
            new_transaction = Transactions(id=trans_id,person_id=person, debit=dbt,credit=crdt)
            new_transaction.save()
            return HttpResponseRedirect(redirect_to=reverse('people'))
        else:
            return render(request,"home/add.html",{"form":form})
    return render(request, "home/add.html",{"form":NewEntryForm()})


def showPerson(request,p_id):
    fname = People.objects.get(pk=p_id).first_name
    lname = People.objects.get(pk=p_id).last_name
    name = fname + ' ' + lname
    transactions = Transactions.objects.filter(person_id=p_id)




    try:
        return render(request, "home/person.html",{
            "transactions":transactions,
            "name": name,
            "exists":True
        })
    except Exception as e:

        print(e, 'herereeerkj', type(transactions))
        return render(request, "home/person.html",{
            "name":name,
            "exists":False
        })