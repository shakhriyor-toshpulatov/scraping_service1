from django import forms

from scraping.models import City, Language


class FindForm(forms.ModelForm):
    city = forms.ModelChoiceField(queryset=City.objects.all(), to_field_name='slug', required=False)
    language = forms.ModelChoiceField(queryset=Language.objects.all(), to_field_name='slug', required=False)
