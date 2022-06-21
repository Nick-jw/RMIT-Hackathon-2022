from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def user_form(request):
    return render(request, 'user_form.html')

def about_us(request):
    template = loader.get_template('about_us.html')
    return HttpResponse(template.render())

