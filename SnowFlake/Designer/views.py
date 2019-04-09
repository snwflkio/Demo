from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from Designer.static.Generate import parseHTML
from Designer.static.Upload import uploadApp

# Create your views here.

class CreateView(TemplateView):
    template_name="index.html"

# This is defined in urls.py 
def generate(request):
    if request.is_ajax():
        name = parseHTML(request.POST['val'])
        uploadApp(name)
    return HttpResponseRedirect('/')
