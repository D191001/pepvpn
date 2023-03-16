# from django.shortcuts import render

from django.views.generic.base import TemplateView


class DownloadView(TemplateView):
    template_name = 'about/download.html'


class HelpView(TemplateView):
    template_name = 'about/help.html'


class DonatView(TemplateView):
    template_name = 'about/donat.html'
