#!/usr/bin/env python
# coding=utf-8
"""Global models shared by all installed apps"""

import inspect
import json

import pymonzo

from django.db import models


class Setting(models.Model):
    """Global settings"""
    moduleName = models.CharField(max_length=32, blank=False, null=False)
    settingName = models.CharField(max_length=32, blank=False, null=False)
    settingValue = models.CharField(max_length=1024, blank=True, null=True)

    @staticmethod
    def get_module(up=1):
        frm = inspect.stack()[up]
        mod = inspect.getmodule(frm[0])
        parts = mod.__name__.split(".")
        if parts[0] == "apps":
            del parts[0]
        return parts[0]

    @staticmethod
    def get_value(key, module=None):
        if module is None:
            module = Setting.get_module(2)
            print("found module " + module)
        return Setting.objects.get(moduleName=module, settingName=key).settingValue

    @staticmethod
    def set_value(key, value, module=None):
        if module is None:
            module = Setting.get_module(2)
            print("found module " + module)
        obj = Setting.objects.get_or_create(moduleName=module, settingName=key)[0]
        obj.settingValue = value
        obj.save()

    @staticmethod
    def get_monzo():
        token_data = Setting.get_value("token_data")
        redirect_url = Setting.get_redirect_uri()
        token_data = json.loads(token_data)
        return pymonzo.MonzoAPI(
            token_data=token_data,
            token_save_function=Setting.save_token_data,
            redirect_url=redirect_url
        )

    @staticmethod
    def get_redirect_uri():
        return "https://" + Setting.get_value("instance_domain") + "/auth"

    @staticmethod
    def save_token_data(monzo):
        token = monzo._token.copy()
        token.update(client_secret=monzo._client_secret)
        Setting.set_value("token_data", json.dumps(token), "monzohosting")


class webhookReceivers(models.Model):
    moduleName = models.CharField(max_length=32, blank=False, null=False)
    webhookType = models.CharField(max_length=32, blank=False, null=False)
    canReceive = models.BooleanField(default=False, blank=False, null=False)
