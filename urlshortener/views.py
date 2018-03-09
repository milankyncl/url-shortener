from django.shortcuts import render, render_to_response
from django.http import Http404, HttpResponseRedirect
from django.template import RequestContext
from .models import Link

# Create your views here.

#
# Úvodní stránka
#

def index(request):
    return render(request, 'index.html')

#
# Přesměrování po načtení odkazu
#

def detail(request, link_code):
    try:
        link = Link.objects.get(code=link_code)
    except Link.DoesNotExist:
        raise  Http404("We are sorry, but link doesn't exist.")
    return HttpResponseRedirect(link.url)

#
# 404, stránka nenalezena
#

def handler404(request):
    response = render_to_response('404.html')
    response.status_code = 404
    return response