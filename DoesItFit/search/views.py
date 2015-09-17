# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView

class SearchView(TemplateView):
    """
    Page permettant de faire une recherche
    """

    template_name="search/search_main.html"
    
    def get_context_data(self, **kwargs):
        """
        Envoi les infos contextuelles au gabarit
        """
        context = super(SearchView, self).get_context_data(**kwargs)
        context['dim_range'] = list(range(10, 150))
        return context

class ResultsView(TemplateView):
    """
    Page permettant d'afficher les résultats
    """
    template_name="search/results.html"

    def get_context_data(self, **kwargs):
        """
        Envoi les infos contextuelles au gabarit
        """
        context = super(ResultsView, self).get_context_data(**kwargs)
        return context
