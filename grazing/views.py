from __future__ import division

from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from django.db.models import Count

from django.contrib.gis.db import models
from django.contrib.gis.geos import *


from grazing.models import *

def index(request):

	states = State.objects.all().order_by('name')

	acreage = State.objects.aggregate(Sum('fieldoffice__allotment__public_acres'))

	all_permits = State.objects.aggregate(total=Count('fieldoffice__permit'))
	exempted_permits = State.objects.filter(fieldoffice__permit__permit_status='FLPMA 402(C)(2)/APPROP ACT').aggregate(total=Count('fieldoffice__permit'))
	exempted_permit_pct = (exempted_permits['total'] / all_permits['total']) * 100

	return render(request, 'base.html', {'states': states, 'acreage': acreage, 'exempted_permit_pct': exempted_permit_pct})

# state by state view, used to generate the descriptions used on the index page of the published graphic
def state(request, state_slug):

	state = State.objects.get(abbr=state_slug)

	#total acres
	acreage = State.objects.filter(abbr=state_slug).aggregate(total=Sum('fieldoffice__allotment__public_acres'))

	#total livestock (thought about using aums ...)
	livestock = State.objects.filter(abbr=state_slug).aggregate(total=Sum('fieldoffice__permit__livestock_number'))

	#total ranchers
	ranchers = State.objects.filter(abbr=state_slug).aggregate(total=Count('fieldoffice__permit__auth_no__operator'))

	#permit renewals
	all_permits = State.objects.filter(abbr=state_slug).aggregate(total=Count('fieldoffice__permit'))
	exempted_permits = State.objects.filter(abbr=state_slug, fieldoffice__permit__permit_status='FLPMA 402(C)(2)/APPROP ACT').aggregate(total=Count('fieldoffice__permit'))
	exempted_permit_pct = (exempted_permits['total'] / all_permits['total']) * 100 # hack to get this into readable pct format

	# acres meeting lhs, acres not evaluated
	lhs_acres_yes = State.objects.filter(abbr=state_slug, fieldoffice__allotment__health__lhs='ALL STANDARDS MET').aggregate(total=Sum('fieldoffice__allotment__public_acres'))
	lhs_filter_categories = ['NO DATA', 'DETERMINATION NOT COMPLETE', '----']
	lhs_acres_unk = State.objects.filter(abbr=state_slug, fieldoffice__allotment__health__lhs__in=lhs_filter_categories).aggregate(total=Sum('fieldoffice__allotment__public_acres'))

	return render(request, 'state_detail.html', {'state': state, 'acreage': acreage, 'livestock': livestock, 'ranchers': ranchers, 'all_permits': all_permits, 'exempted_permits': exempted_permits, 'exempted_permit_pct': exempted_permit_pct, 'lhs_acres_yes': lhs_acres_yes, 'lhs_acres_unk': lhs_acres_unk})


def allotment(request, allotment_unique):

	boundary = Health.objects.get(allotment_unique=allotment_unique)

	allot = Allotment.objects.get(allotment_unique=allotment_unique)
	total_acres = Allotment.objects.filter(allotment_unique=allotment_unique).aggregate(total=Sum('public_acres'))

	ranchers = Allotment.objects.filter(allotment_unique=allotment_unique).aggregate(total=Count('auth_no__operator__id'))

	permits = Permit.objects.filter(allotment__allotment_unique=allotment_unique)
	all_permits = Permit.objects.filter(allotment__allotment_unique=allotment_unique).aggregate(total=Count('id'))

	exempted_permits = Permit.objects.filter(allotment__allotment_unique=allotment_unique, permit_status='FLPMA 402(C)(2)/APPROP ACT').aggregate(total=Count('id'))
	exempted_permit_pct = (exempted_permits['total'] / all_permits['total']) * 100 # hack to get this into readable pct format



	operators = Operator.objects.filter(auth_no__permit__allotment__allotment_unique=allotment_unique).distinct()

	auths = allot.auth_no.all()

	health = allot.health_set.all()

	return render(request, 'allotment_detail.html',
		{
		'allot': allot,
		'auths': auths,
		'health': health,
		'operators': operators,
		'boundary': boundary,
		'total_acres': total_acres,
		'ranchers': ranchers,
		'permits': permits,
		'all_permits': all_permits,
		'exempted_permits': exempted_permits,
		'exempted_permit_pct': exempted_permit_pct,

			})
