from django.shortcuts import render

from.models import Company

def home(request):
	name = Company.objects.all
	return render(request,'home.html',{'name':name})
