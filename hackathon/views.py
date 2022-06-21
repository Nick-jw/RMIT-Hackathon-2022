from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.db.models import Avg
from .forms import InputForm
from .models import Companies, Users

# Create your views here.
from django.http import HttpResponse


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def about_us(request):
    template = loader.get_template('about_us.html')
    return HttpResponse(template.render())

def user_form(request):
    if request.method == "POST":
        form = InputForm(request.POST)

        if form.is_valid():
    
            company = Companies.objects.get(
                stock_code=form.cleaned_data['company_name'])

            user = Users()

            user.stock_code = company
            user.role = form.cleaned_data['role']
            user.gender = form.cleaned_data['gender']
            user.salary_band = form.cleaned_data['salary_band']
            user.Q1 = form.cleaned_data['question_1']
            user.Q2 = form.cleaned_data['question_2']
            user.Q3 = form.cleaned_data['question_3']
            user.Q4 = form.cleaned_data['question_4']
            user.Q5 = form.cleaned_data['question_5']
            user.Q6 = form.cleaned_data['question_6']
            user.Q7 = form.cleaned_data['question_7']
            user.Q8 = form.cleaned_data['question_8']
            user.Q9 = form.cleaned_data['question_9']
            user.Q10 = form.cleaned_data['question_10']

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
    
    # APT afterpay
    
    form_data = Users.objects.filter(stock_code__exact = '7')
    comp_data = Companies.objects.all()
    
    Q1avg_male = Users.objects.filter(stock_code__exact = '7', gender__exact = 'M').aggregate(Avg("Q1"))['Q1__avg']
    
    Q1avg_female = Users.objects.filter(stock_code__exact = '7', gender__exact = "F").aggregate(Avg("Q1"))['Q1__avg']
    
    Q2avg = Users.objects.filter(stock_code__exact = '7').aggregate(Avg("Q2"))['Q2__avg']

    Q3avg = Users.objects.filter(stock_code__exact = '7').aggregate(Avg("Q3"))['Q3__avg']

    Q4avg = Users.objects.filter(stock_code__exact = '7').aggregate(Avg("Q4"))['Q4__avg']

    Q5avg = Users.objects.filter(stock_code__exact = '7').aggregate(Avg("Q5"))['Q5__avg']

    Q6avg = Users.objects.filter(stock_code__exact = '7').aggregate(Avg("Q6"))['Q6__avg']

    Q7avg = Users.objects.filter(stock_code__exact = '7').aggregate(Avg("Q7"))['Q7__avg']

    Q8avg = Users.objects.filter(stock_code__exact = '7').aggregate(Avg("Q8"))['Q8__avg']

    Q9avg = Users.objects.filter(stock_code__exact = '7').aggregate(Avg("Q9"))['Q9__avg']

    
    form_ctx = {
        'formData': form_data,
        'Q1avg_male': Q1avg_male,
        'Q1avg_female': Q1avg_female,
        'Q2avg': Q2avg,
        'Q3avg': Q3avg,
        'Q4avg': Q4avg,
        'Q5avg': Q5avg,
        'Q6avg': Q6avg,
        'Q7avg': Q7avg,
        'Q8avg': Q8avg,
        'Q9avg': Q9avg
        }

    return render(request, 'company.html', form_ctx)
