from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member


# Create your views here.
"""HOME"""
def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())


"""
This functionality response with all members
"""
def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        "mymembers" : mymembers
    }
    return HttpResponse(template.render(context,request))

"""
This functionality responds with details of a member with an id from the url params
"""
def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('member_details.html')
    context = {
        "mymember" : mymember
    }
    return HttpResponse(template.render(context,request))
