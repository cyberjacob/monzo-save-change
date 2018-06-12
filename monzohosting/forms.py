#!/usr/bin/env python
# coding=utf-8

from django import forms


class SetupForm(forms.Form):
    client_id = forms.CharField()
    client_secret = forms.CharField()
    instance_domain = forms.CharField()
