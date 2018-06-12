from django.views.generic import DetailView, TemplateView

from monzohosting import models


# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        try:
            monzo = models.Settings.get_monzo()
        except models.Settings.DoesNotExist:
            return {'error': True, 'message': "No Monzo configuration available."}
        return {'error': False, 'message': monzo.whoami()}
