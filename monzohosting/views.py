#!/usr/bin/env python
# coding=utf-8
import pymonzo
from django.views.generic import FormView, TemplateView, RedirectView

from monzohosting import models, forms


# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        try:
            monzo = models.Settings.get_monzo()
        except models.Settings.DoesNotExist:
            return {'error': True, 'message': "No Monzo configuration available."}
        return {'error': False, 'message': monzo.whoami()}


class SetupView(FormView):
    template_name = "setup.html"
    form_class = forms.SetupForm

    def form_valid(self, form):
        models.Settings.set_value("client_id", form.cleaned_data["client_id"])
        models.Settings.set_value("client_secret", form.cleaned_data["client_secret"])
        models.Settings.set_value("instance_domain", form.cleaned_data["instance_domain"])
        SetupView.success_url = "https://auth.getmondo.co.uk/?response_type=code&redirect_uri=https://" + \
                                form.cleaned_data["instance_domain"] + "/auth&client_id=" + \
                                form.cleaned_data["client_id"]
        return super().form_valid(form)


class AuthView(RedirectView):
    def get(self, request, *args, **kwargs):
        pymonzo.MonzoAPI(
            client_id=models.Settings.get_value("client_id"),
            client_secret=models.Settings.get_value("client_secret"),
            redirect_url="https://" + models.Settings.get_value("instance_domain") + "/auth",
            token_save_function=models.Settings.save_token_data
        )

        return super().get(request, *args, **kwargs)
