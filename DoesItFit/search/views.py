# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView

class SearchView(TemplateView):

    template_name="search/search_main.html"