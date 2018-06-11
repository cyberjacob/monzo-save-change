from django.views.generic import DetailView

from monzohosting import models


# Create your views here.
class IndexView(DetailView):

    def get_queryset(self):
        try:
            monzo = models.Settings.get_monzo()
        except models.Settings.DoesNotExist:
            return {'error': True, 'message': "No Monzo configuration available."}
        return {'error': False, 'message': monzo.whoami()}
