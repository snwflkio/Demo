from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from Designer.static.test import generate_test
from Designer.static.Generate import parseHTML

# Create your views here.

class CreateView(TemplateView):
    template_name="index.html"

# This is defined in urls.py 
def generate(request):

    if request.is_ajax():
        print("AJAX REQUEST!")
        print(request.POST['val'])
        parseHTML(request.POST['val'])
    return HttpResponseRedirect('/')
