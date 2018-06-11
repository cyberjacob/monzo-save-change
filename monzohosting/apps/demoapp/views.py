from django.http import HttpResponse
from django.views import View
from monzohosting.monzohosting import models

# Create your views here.
class IndexView(View):
    def get(self, request):
        module_name = models.Settings.debug_print_module()
        return HttpResponse(module_name)
