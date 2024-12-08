from django.http import HttpResponse
from django.template import loader

# Create your views here.
def principal(request):
    template = loader.get_template('principal.html')
    return HttpResponse(template.render())