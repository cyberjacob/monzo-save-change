#!/usr/bin/env python
# coding=utf-8
from django.views.generic import TemplateView

from monzohosting import models


# Create your views here.
class IndexView(TemplateView):
    template_name = "demoapp_index.html"

    def get_context_data(self, **kwargs):
        monzo = models.Settings.get_monzo()
        accounts = monzo.accounts()
        c = {}
        for account in accounts:
            c[account.id] = monzo.balance(account.id).balance
        return {'accounts': c}
