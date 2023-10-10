from django.http import HttpResponse
from django.template import loader
from .models import Member
# Create your views here

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def member(request):
    mymembers=Member.objects.all().values()
    template = loader.get_template('allMembers.html')
    context = {
        'mymembers' : mymembers,
    }
    return HttpResponse(template.render(context,request))

def details(request,slug):
    mymember=Member.objects.get(slug=slug)
    template = loader.get_template('details.html')
    context = {
        'mymember' : mymember,
    }
    return HttpResponse(template.render(context,request))

def testing(request):
    mydata = Member.objects.values_list('firstName')
    template = loader.get_template('template.html')
    context = { 
        'myMembers':mydata
    }
    return HttpResponse(template.render(context,request))
    