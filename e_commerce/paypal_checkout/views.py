from models.ipn_endpoint import Endpoint
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@require_POST
@csrf_exempt
def ipn_endpoint(request):
    print "LALALALALALALALALALALALALALALALALALALALALALA"
    Endpoint().__call__(request)