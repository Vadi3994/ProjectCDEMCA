from django.shortcuts import render

# Create your views here.
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
    return render(request, 'Web_App/blog-home.html')

def singleblog(request):
    return render(request, 'Web_App/single-blog.html')

def agents(request):
    return render(request, 'Web_App/agents.html')

def elements(request):
    return render(request, 'Web_App/elements.html')

def contact(request):
    return render(request, 'Web_App/contact.html')