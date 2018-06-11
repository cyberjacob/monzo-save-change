from django.http import HttpResponse
from django.views import View
from monzohosting import models

# Create your views here.
class IndexView(View):
    def get(self, request):
        module_name = models.Settings.get_module()
        models.Settings.getValue("test")
        return HttpResponse(module_name)
