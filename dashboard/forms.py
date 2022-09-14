from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Submit, Column
from .models import *


class ProfileForm(forms.Form):
    address1 = forms.CharField(required=True, label='Address Line 1', widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Address Line1'}))
    address2 = forms.CharField(required=False, label='Address Line 2', widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Address Line2'}))
    city = forms.CharField(required=True, label='City', widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Enter City'}))
    province = forms.CharField(required=True, label='Province', widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Province'}))
    country = forms.CharField(required=True, label='Country', widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Country'}))
    postalCode = forms.CharField(required=True, label='Postal Code', widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Postal Code'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
        Row(Column('address1', css_class='form-group col-md-6'),
            Column('address2', css_class='form-group col-md-6')),
        Row(Column('city', css_class='form-group col-md-6'),
            Column('province', css_class='form-group col-md-6')),
        Row(Column('country', css_class='form-group col-md-6'),
            Column('postalCode', css_class='form-group col-md-6')),
        Submit('submit', 'Save Changes', css_class='button white'),
    )


class Meta:
    model: Profile
    fields: ['address1', 'address2', 'city',
             'province', 'country', 'postalCode']
