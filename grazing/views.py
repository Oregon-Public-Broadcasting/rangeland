from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from django.db.models import Count

from grazing.models import *

def index(request):
	return render(request, 'base.html')

def allotment(request, allotment_unique):
	allot = Allotment.objects.get(allotment_unique=allotment_unique)
	auths = allot.auth_no.all()

	operators = []

	for a in auths:
		o = a.operator_set.all()


		operators.extend(o)


	health = allot.health_set.all()


	return render(request, 'allotment_detail.html', {'allot': allot, 'auths': auths, 'health': health, 'operators': operators})



# Create your views here.
# Create your views here.
#from django.http import HttpResponseRedirect
