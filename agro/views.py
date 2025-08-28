from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.template import loader

from .models import CommodityType, CommodityCategory, District, PestAlertLevel, PestRiskEntryStart, PestRiskEntry

from django_tables2 import RequestConfig
from .tables import PestRiskListTable

#from .serializers import CommodityTypeSerializer, CommodityCategorySerializer
from . import serializers as sx

from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from wimp.serializers import GroupSerializer, UserSerializer

from .forms import  FormPestRiskStartForm, PestRiskEntryForm, PestRiskEntryFormDetails

#################### Create/Define Views ####################
def index(request):
    template = loader.get_template('agro_services.html')
    context = {'name': 'World'}  # Data to pass to the template
    return HttpResponse(template.render(context))
  
def livestock_entry(request):
    template = loader.get_template('entry_form_livestock.html')
    context = {'name': 'World'}  # Data to
    return HttpResponse(template.render(context))    

def pest_risk_list(request):
    #pr_data = PestRiskEntry.objects.all()
    #return render(request, "pest_risk_list.html", {"pest_risk_data": pr_data })
    #template = loader.get_template('pest_risk_list.html')
    #context = {}  # Data to pass to the template
    #return HttpResponse(template.render(context))
    table = PestRiskListTable(PestRiskEntry.objects.all())
    RequestConfig(request).configure(table)
    return render(request, "pest_risk_list.html", {"table": table})

def edit_pest_risk_entry(request, entry_id):
    #frm_pest_risk = PestRiskEntryForm()
    #return render(request, 'entry_form_pest_risk.html', {"form": frm_pest_risk})
    
    entry = get_object_or_404(PestRiskEntryStart, id = entry_id)

    if request.method == 'POST':
        form = PestRiskEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('pest_risk_entry_start', entry_id = entry.id)
    else:
        form = PestRiskEntryForm(instance=entry)  # <-- pre-fills the form

    return render(request, 'entry_form_pest_risk.html', {'form': form })

def pest_risk_entry_start_view(request):
    frm_pest_risk_start = FormPestRiskStartForm(request.POST)

    if frm_pest_risk_start.is_valid():
        selected = frm_pest_risk_start.cleaned_data['list_months']
        return render(request, 'entry_form_pest_risk_start.html', { 'selected': selected })
    else:
        frm_pest_risk_start = FormPestRiskStartForm()

    return render(request, 'entry_form_pest_risk_start.html', { 'form' : frm_pest_risk_start })

def pest_risk_entry_start_add_view(request):
    
    if request.method == 'POST':
        form = FormPestRiskStartForm(request.POST)
        if form.is_valid():
            # Get cleaned data
            months      = form.cleaned_data['list_months']
            commodity   = form.cleaned_data['lst_commodity']
            year        = form.cleaned_data['year']

            # Save to DB
            entry = PestRiskEntryStart.objects.create(
                months          = months,         # list gets stored in JSONField
                commodity_id    = commodity,
                year            = year
            )
            return redirect('pest_risk_entry_details', entry_id = entry.id)  # replace with your success page/view
            #return render(request, 'entry_form_pest_risk.html', { 'entry_id': new_id })
    else:
        form = FormPestRiskStartForm()
    return render(request, 'entry_form_pest_risk_start.html', {'form': form })

def pest_risk_entry_details(request, entry_id):

    form = PestRiskEntryFormDetails(request.POST or None, entry_id=entry_id)

    if request.method == 'POST':
    
        if form.is_valid():
            #selected = frm_pest_risk_details.cleaned_data['list_months']
            #return render(request, 'entry_form_pest_risk.html', { 'selected': selected })
        
            selected = form.cleaned_data.get('list_months')

            return render(request, 'entry_form_pest_risk.html', { 
                'selected': selected, 'form': form, 'pest_risk_start_id': entry_id
            })
        else:
            form = PestRiskEntryFormDetails(entry_id=entry_id)

    return render(request, 'entry_form_pest_risk.html', { 'form': form,'pest_risk_start_id': entry_id })

def pest_risk_entry_add_details(request, entry_id):
    
    if request.method == 'POST':
        form = PestRiskEntryFormDetails(request.POST)
        if form.is_valid():
            # Get cleaned data
            pest_risk_start_id = form.cleaned_data['pest_risk_start_id']
            district_id         = form.cleaned_data['district_id']
            drought_alert_lvl_id = form.cleaned_data['drought_alert_lvl_id']
            temp_min        = form.cleaned_data['temp_min']
            temp_max        = form.cleaned_data['temp_max']
            precip_min  = form.cleaned_data['precip_min']
            precip_max  = form.cleaned_data['precip_max']
            effect      = form.cleaned_data['effect']
            actions     = form.cleaned_data['actions']
            info        = form.cleaned_data['info']

            # Save to DB
            entry = PestRiskEntry.objects.create(
                pest_risk_start_id  = pest_risk_start_id,
                district_id         = district_id,         # list gets stored in JSONField
                drought_alert_lvl_id = drought_alert_lvl_id,
                temp_min        = temp_min,
                temp_max        = temp_max,
                precip_min      = precip_min,
                precip_max      = precip_max,
                effect          = effect,
                actions         = actions,
                info            = info
            )
            return redirect('pest_risk_list')  # replace with your success page/view
    else:
        form = FormPestRiskStartForm()
    return render(request, 'entry_form_pest_risk.html', {'form': form })

#################### Form Processing ####################


#API endpoint that allows groups to be viewed or edited.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

#API endpoint that allows groups to be viewed or edited.
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

#API endpoint that allows groups to be viewed or edited.
class DistrictViewSet(viewsets.ModelViewSet):
   queryset = District.objects.all().order_by('id')
   serializer_class = sx.DistrictSerializer

class CommodityTypeViewSet(viewsets.ModelViewSet):
   queryset = CommodityType.objects.all().order_by('id')
   serializer_class = sx.CommodityTypeSerializer

class CommodityCategoryViewSet(viewsets.ModelViewSet):
   queryset = CommodityCategory.objects.all().order_by('id')
   serializer_class = sx.CommodityCategorySerializer

class PestAlertLevelViewSet(viewsets.ModelViewSet):
   queryset = PestAlertLevel.objects.all().order_by('id')
   serializer_class = sx.PestAlertLevelSerializer

class PestRiskEntryViewSet(viewsets.ModelViewSet):
   queryset = PestRiskEntry.objects.all().order_by('id')
   serializer_class = sx.PestRiskEntrySerializer