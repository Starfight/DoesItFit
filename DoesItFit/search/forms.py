# -*- coding: utf-8 -*-
"""
Fichier des formulaires
"""
from django import forms

class SearchForm(forms.Form):
	"""
	Formulaire de recherche
	"""
	# liste des mesures
	list_mesures = [(str(s)+" cm", s) for s in range(10, 151)]
	list_mesures.insert(0, ("Indifferent", 0))

	# champs du formulaire
    search_subject = forms.CharField(label='Subject', required=False, max_length=100)
    search_lenght = forms.ChoiceField(label='Lenght', choices=list_mesures, required=False)
    search_width = forms.ChoiceField(label='Width', choices=list_mesures, required=False)
    search_height = forms.ChoiceField(label='Height', choices=list_mesures, required=False)