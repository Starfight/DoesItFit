# -*- coding: utf-8 -*-
"""
Fichier des formulaires
"""
from django import forms
from django.utils.translation import ugettext as _

class SearchForm(forms.Form):
    """
    Formulaire de recherche
    """
    # classe CSS
    css_class = "form-control"
    
    # placeholder
    placeholder = _("What do you want to search?")
    
    # liste des mesures
    list_mesures = [(s, str(s)+" cm") for s in range(10, 151)]
    list_mesures.insert(0, (None, _("Indifferent")))

    # champs du formulaire
    search_subject = forms.CharField(label='Subject', required=False, max_length=100 , widget=forms.TextInput(attrs={"class": css_class, "placeholder": placeholder, "autofocus":True}))
    search_lenght = forms.ChoiceField(label='Lenght', choices=list_mesures, required=False, widget=forms.Select(attrs={"class": css_class}))
    search_width = forms.ChoiceField(label='Width', choices=list_mesures, required=False, widget=forms.Select(attrs={"class": css_class}))
    search_height = forms.ChoiceField(label='Height', choices=list_mesures, required=False, widget=forms.Select(attrs={"class": css_class}))