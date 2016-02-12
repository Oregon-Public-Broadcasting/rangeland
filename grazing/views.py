from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from django.db.models import Count

from grazing.models import *


def index(request):

	return render(request, 'base.html')


# Create your views here.
# Create your views here.
#from django.http import HttpResponseRedirect
