# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView

class SearchView(TemplateView):

    template_name="search/search_main.html"
    
    def get_context_data(self, **kwargs):
        """
        Envoi les infos contextuelles au gabarit
        """
        context = super(SearchView, self).get_context_data(**kwargs)
        context['dim_range'] = list(range(10, 150))
        return context
