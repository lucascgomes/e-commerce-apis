from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response


def index(request):
	context = RequestContext(request)
	return render_to_response('donation/index.html', {}, context)



# Create your views here.
