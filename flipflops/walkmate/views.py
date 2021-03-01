from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def shoes(request):
    return HttpResponse('best offers are arrived here')
