from django.shortcuts import render
from django.views.generic import TemplateView


class GraphView(TemplateView):
    template_name = 'random_generator/graph.html'
