from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.template import loader

from .models import Family


def saludar(request, nombre):
    print(nombre)
    return HttpResponse('<h1>Hola '+ nombre +'</h1>')

def index(request):
    family_list = Family.objects.all()
    template = loader.get_template('family/index.html')
    context = {
        'family_list': family_list,
    }
    return HttpResponse(template.render(context, request))

def create_family_member_form(request):
    print(request.method)
    template = loader.get_template('family/create.html')
    return HttpResponse(template.render({}, request))

def create_family_member(request):
    if request.method == "POST":
        print(request.POST)
        new_name = request.POST['fname'] + ' ' + request.POST['lname']
        print(new_name)
        f = Family(name=new_name)
        f.save()
        return HttpResponsePermanentRedirect("/")    
    return HttpResponse("Not POST")