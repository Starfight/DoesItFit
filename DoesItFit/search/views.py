# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
from DoesItFit.search.forms import SearchForm
from DoesItFit.search.models import Article


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

    def get_context_data(self, **kwargs):
        """
        Envoi les infos contextuelles au gabarit
        """
        context = super(ResultsView, self).get_context_data(**kwargs)
        context["articles_list"] = Article.objects.all()
        return context
