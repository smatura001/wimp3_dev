from django import forms
from .models import Months, CommodityType, DroughtAlertLevel, District, PestRiskEntryMainListing, PestRiskEntryDetails,  PestAlertLevel, PestRiskEffect, PestRiskAction

MONTH_CHOICES = [
    ('1','JAN'),
    ('2', 'FEB'),
    ('3','MAR'),
    ('4','APR'),
    ('5','MAY'),
    ('6','JUN'),
    ('7','JUL'),
    ('8','AUG'),
    ('9','SEP'),
    ('10','OCT'),
    ('11','NOV'),
    ('12','DEC')
]

class FormPestRiskStartForm(forms.Form):
    months = forms.MultipleChoiceField(
        choices = MONTH_CHOICES,
        widget = forms.CheckboxSelectMultiple(
            attrs={'class': 'form-check-input'}
        ),
        required = True
    )
    commodity = forms.ModelChoiceField(
        queryset = CommodityType.objects.all(),
        empty_label = "Select a Commodity",
        required = True,
        widget = forms.Select(attrs = {'class': 'form-control' })
    )
    year = forms.CharField(
        label = "Year",
        required = True,
        max_length = 4,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Year'})
    )

    def clean_months(self):
        months = self.cleaned_data.get("months", [])
        if len(months) > 3:
            raise forms.ValidationError("You can only select up to 3 months.")
        return months

class PestRiskMainListingForm(forms.ModelForm):
    class Meta:
        model = PestRiskEntryMainListing
        fields = ['months', 'year', 'commodity']
        labels = {   
            # <-- add human-friendly labels here
            'months': 'Select Months',
            'year': 'Year:',
            'commodity': 'Commodity',
        }
        widgets = {
            #id': forms.HiddenInput(),
            'months': forms.CheckboxSelectMultiple(
                choices=MONTH_CHOICES,
                attrs={'class': 'form-check-input'}
            ),
            'year': forms.TextInput(attrs={'class': 'form-control'}),
            'commodity': forms.Select(attrs={'class': 'form-control'})
        }


class PestRiskEntryFormDetails(forms.ModelForm):
    class Meta:
        model = PestRiskEntryDetails
        fields = ['pest_risk_listing_id', 'district_id', 'drought_alert_lvl_id','temp_max','temp_min','precip_min','precip_max','effect','info','actions']
        labels = {   
            'district_id': 'Select District / Zone',
            'drought_alert_lvl_id': 'Drought Level Alert:',
            'temp_min': 'TEMP MIN (°F):',
            'temp_max': 'TEMP MAX (°F):',
            'precip_min': 'PRECIP MIN (mm):',
            'precip_max': 'PRECIP MAX (mm):',
            'effect': 'Possible Effect:',
            'info': 'Additional Info for Possible Effect:',
            'actions': 'Actions:'
        }
        widgets = {
            'pest_risk_listing_id': forms.HiddenInput(),
            'district_id':  forms.Select(attrs={'class': 'form-control'}),
            'drought_alert_lvl_id': forms.Select(attrs={'class': 'form-control'}),
            'temp_min': forms.TextInput(attrs={'class': 'form-control'}),
            'temp_max': forms.TextInput(attrs={'class': 'form-control'}),
            'precip_min': forms.TextInput(attrs={'class': 'form-control'}),
            'precip_max': forms.TextInput(attrs={'class': 'form-control'}),
            'effect': forms.Select(attrs={'class': 'form-control'}),
            'info': forms.Textarea(attrs={'class': 'form-control'}),
            'actions': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):

        entry_id = kwargs.pop('entry_id',None)
        super().__init__(*args,**kwargs)

        # set hidden entry_id if provided
        if entry_id is not None:
            self.fields['pest_risk_listing_id'].initial = entry_id

        # ensure dropdown is populated from PestAlertLevel model
        self.fields['district_id'].queryset = District.objects.all().order_by("id")
        self.fields['district_id'].empty_label = "Select District / Zone"
        
        self.fields['drought_alert_lvl_id'].queryset = DroughtAlertLevel.objects.all().order_by("id")
        self.fields['drought_alert_lvl_id'].empty_label = "Select Drought Alert Level"
        self.fields['drought_alert_lvl_id'].label_from_instance = lambda obj: obj.title

        self.fields['effect'].queryset = PestRiskEffect.objects.all().order_by("id")
        self.fields['effect'].empty_label = "Possible Effects"

        self.fields['actions'].queryset = PestRiskAction.objects.all().order_by("id")
        self.fields['actions'].empty_label = "Select Actions"


class PestAlertLevelForm(forms.ModelForm):
    class Meta:
        model = PestAlertLevel
        fields = ['description', 'color_hex']
        labels = {   
            # <-- add human-friendly labels here
            'description': 'Description:',
            'color_hex': 'Color HEX',
        }
        widgets = {            
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'color_hex': forms.TextInput(attrs={'class': 'form-control'})
        }

class DroughtAlertLevelForm(forms.ModelForm):
    class Meta:
        model = PestAlertLevel
        fields = ['description', 'color_hex']
        labels = {   
            # <-- add human-friendly labels here
            'description': 'Description:',
            'action_level': 'Action Level:',
            'color_hex': 'Color HEX',
        }
        widgets = {            
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'action_level': forms.TextInput(attrs={'class': 'form-control'}),
            'color_hex': forms.TextInput(attrs={'class': 'form-control'})
        }