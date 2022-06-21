from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from hackathon.models import Companies, Users
from .forms import InputForm
from .models import Companies, Users

# Create your views here.
from django.http import HttpResponse


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def user_form(request):
    if request.method == "POST":
        form = InputForm(request.POST)

        if form.is_valid():

            company = Companies.objects.get(stock_code='AGL')

            print(company.stock_code)
            user = Users()
            user.stock_code = company
            user.Q1 = form.cleaned_data['question_1']
            user.Q2 = form.cleaned_data['question_2']
            user.Q3 = form.cleaned_data['question_3']
            user.Q4 = form.cleaned_data['question_4']
            user.Q5 = form.cleaned_data['question_5']

            user.save()

            # print(form.cleaned_data)
            # for i in form.cleaned_data:
            #    print(i)
            return HttpResponseRedirect('/admin/')
    else:
        context = {}
        context['form'] = InputForm()
        return render(request, "user_form.html", context)
    
def company(request):
    form_data = Users.objects.all()
    comp_data = Companies.objects.all()
    
    form_ctx = {'formData': form_data}
    comp_ctx = {'compData': comp_data}
    return render(request, 'company.html', form_ctx)
