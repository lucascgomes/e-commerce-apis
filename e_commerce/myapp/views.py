from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from e_commerce.settings import PAYPAL_MERCHANT_ID, PAYPAL_HOST, PAYPAL_ENVIRONMENT


def index(request):
	context = RequestContext(request)

	context_dict = {
		'PAYPAL_HOST':PAYPAL_HOST,
		'PAYPAL_MERCHANT_ID':PAYPAL_MERCHANT_ID,
		'PAYPAL_ENVIRONMENT':PAYPAL_ENVIRONMENT,
		'price_amount':10.0,
		'product_name':'Gift Card',
		}
	return render_to_response('myapp/index.html', context_dict, context)





# Create your views here.
