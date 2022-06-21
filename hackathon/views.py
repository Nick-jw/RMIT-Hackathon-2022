from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .forms import InputForm

# Create your views here.
from django.http import HttpResponse


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def user_form(request):
    if request.method == "POST":
        form = InputForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            for i in form.cleaned_data:
                print(i)
            return HttpResponseRedirect('/admin/')
    else:
        context = {}
        context['form'] = InputForm()
        return render(request, "user_form.html", context)
