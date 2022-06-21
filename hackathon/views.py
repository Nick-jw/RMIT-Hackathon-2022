from django.shortcuts import render
from django.template import loader
from hackathon.models import Companies, Users

# Create your views here.
from django.http import HttpResponse


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def user_form(request):
    return render(request, 'user_form.html')

def company(request):
    form_data = Users.objects.all()
    comp_data = Companies.objects.all()
    
    form_ctx = {'formData': form_data}
    comp_ctx = {'compData': comp_data}
    return render(request, 'company.html', form_ctx)

