
from django.shortcuts import render

def about(request):
    #return HttpResponse('this is about page')
    return render(request, 'about.html')

def home(request):
    #return HttpResponse('this is the homepage')
    return render(request, 'homepage.html')