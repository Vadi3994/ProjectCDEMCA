import os
from django.shortcuts import render
from Web_App.models import PropertyDetails
from django.http import HttpResponse

def searchresult(request):
    propdetail = PropertyDetails.objects.all()
    return render(request, 'Web_App/elements.html', {'propdetail': propdetail})

def home(request):
    return render(request, 'Web_App/index.html')

def login(request):
    return render(request, 'Web_App/login.html')

def signup(request):
    return render(request, 'Web_App/signup.html')

def properties(request):
    return render(request, 'Web_App/properties.html')

def about(request):
    return render(request, 'Web_App/about.html')

def bloghome(request):
    command = 'jupyter --execute --allow-errors GenerateRGraphs.ipynb'
    os.system(command)
    return render(request, 'Web_App/RData.html')

def singleblog(request):
    return render(request, 'Web_App/single-blog.html')

def agents(request):
    return render(request, 'Web_App/agents.html')

def elements(request):
    return render(request, 'Web_App/elements.html')

def contact(request):
    return render(request, 'Web_App/contact.html')

