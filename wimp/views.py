from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
#from django import forms
#from .forms import FormPestRisk

# Create your views here.
def index(request):
    return HttpResponse("Welcome Localhost")

#def home(request):
 #   return HttpResponse("Welcome Dashboard")

#################### Form Processing ####################
'''def add_pest_risk_entry_submit(request):
    if request.method == 'POST':  # form was submitted
        form = FormPestRisk(request.POST)  # bind data
        if form.is_valid():  # validation step
            form.save()  # process form: save to DB
            return redirect('book_success')  # redirect after success
        else:
            # form has errors, will be shown in template
            pass
    else:
        form = FormPestRisk()  # GET request → show empty form

    return render(request, 'add_pest_risk_entry.html', {'form': form})'''