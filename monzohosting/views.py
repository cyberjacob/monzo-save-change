from django.http import HttpResponse
from django.views import View
from monzohosting import models

# Create your views here.
class IndexView(View):
    def get(self, request):
        return HttpResponse(models.Settings.get_monzo().whoami())
