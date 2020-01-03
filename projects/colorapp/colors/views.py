from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from colors.get_colors import get_rgb
from django.urls import reverse
import json

from colors.forms import GetHexForm


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


def index(request):
    return HttpResponse("Hello, world. You're at the index.")


def test(request):
    return HttpResponse("This is a test response giving 7 Viridis colors:\n{}".format('\n'.join(get_rgb())))


def test_p(request, colormap='viridis', n=7, flip=False):
    return HttpResponse("This is a test response giving {} {} colors:\n{}".format(n, colormap, '\n'.join(get_rgb(n=n, colormap=colormap, flip=flip))))

def color_json(request, colormap='viridis', n=7, flip=False):
    d = {}
    d[colormap] = repr(dict(zip(range(0, n), get_rgb(n=n, colormap=colormap, flip=flip))))
    return HttpResponse(json.dumps(d))


def hex_form(request):
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = GetHexForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # redirect to a new URL:
            #return HttpResponseRedirect(reverse('api', kwargs=form.cleaned_data))
            #return result(request, **form.cleaned_data)

            context = {
                'form': form,
                'colors': dict(zip(range(0, form.cleaned_data['n']), get_rgb(**form.cleaned_data)))
            }
            return render(request, 'colorpage-results.html', context)

    # If this is a GET (or any other method) create the default form.
    else:
        form = GetHexForm()

    context = {
        'form': form,
    }

    return render(request, 'colorpage.html', context)
