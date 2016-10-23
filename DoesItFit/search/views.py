# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
from DoesItFit.search.forms import SearchForm
from django.http import HttpResponseRedirect

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
        context['form'] = SearchForm()
        return context

class ResultsView(TemplateView):
    """
    Page permettant d'afficher les résultats
    """
    template_name="search/results.html"

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return super(ResultsView, self).render_to_response(context)
        
    def get(self, request, *args, **kwargs):
        """
        GET methode
        """
        # vérifie qu'on est en GET
        if request.method == 'GET':
            # crée le formulaire à partir des données
            form = SearchForm(request.GET)
            # vérifie la validité
            if form.is_valid():
                # obtient les informations
                lenght = form.cleaned_data['search_lenght']
                width = form.cleaned_data['search_width']
                height = form.cleaned_data['search_height']
                subject = form.cleaned_data['search_subject']
                
                # requete les données
                
                context = self.get_context_data(**kwargs)
                # return HttpResponse(form.cleaned_data['search_subject'])
                return super(ResultsView, self).render_to_response(context)
        
        # erreur retour case départ
        return HttpResponseRedirect("/")
        
    def get_context_data(self, **kwargs):
        """
        Envoi les infos contextuelles au gabarit
        """
        context = super(ResultsView, self).get_context_data(**kwargs)
        return context
