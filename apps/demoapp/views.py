from django.http import HttpResponse
from django.views import View
from monzohosting import models

# Create your views here.
class IndexView(View):
    def get(self, request):
        module_name = models.Settings.get_module()
        try:
            models.Settings.getValue("test")
        except models.Settings.DoesNotExist:
            pass
        return HttpResponse(module_name)
