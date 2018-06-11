#!/usr/bin/env python
# coding=utf-8
"""Global models shared by all installed apps"""

import inspect
import json

import pymonzo

from django.db import models


class Settings(models.Model):
    """Global settings"""
    # TODO: Make settings available to modules
    moduleName = models.CharField(max_length=32, blank=False, null=False)
    settingName = models.CharField(max_length=32, blank=False, null=False)
    settingValue = models.CharField(max_length=128, blank=True, null=True)

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
            module = Settings.get_module(2)
            print("found module " + module)
        return Settings.objects.get(moduleName=module, settingName=key).settingValue

    @staticmethod
    def set_value(key, value, module=None):
        if module is None:
            module = Settings.get_module(2)
            print("found module " + module)
        obj = Settings.objects.get(moduleName=module, settingName=key)
        obj.settingValue = value
        obj.save()

    @staticmethod
    def get_monzo():
        token_data = Settings.get_value("token_data")
        redirect_url = Settings.get_value("redirect_url")
        token_data = json.loads(token_data)
        return pymonzo.MonzoAPI(
            token_data=token_data,
            token_save_function=Settings.save_token_data,
            redirect_url=redirect_url
        )

    @staticmethod
    def save_token_data(monzo):
        token = monzo._token.copy()
        token.update(client_secret=monzo._client_secret)
        Settings.set_value("token_data", json.dumps(token))
