<<<<<<< HEAD
from models.ipn_endpoint import Endpoint
=======
from paypal_ipn import Endpoint
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
>>>>>>> 1fafb87d93b747deb16bd78d158015433593c8f5
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@require_POST
@csrf_exempt
def ipn_endpoint(request):
    print "LALALALALALALALALALALALALALALALALALALALALALA"
    Endpoint().__call__(request)
    return HttpResponse("OKAY")

def auto_return(request):
    context = RequestContext(request)
    return render_to_response('paypal_checkout/return_page.html', {}, context)
