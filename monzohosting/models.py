#!/usr/bin/env python
# coding=utf-8
"""Global models shared by all installed apps"""

import inspect

from django.db import models


class Settings(models.Model):
    """Global settings"""
    #TODO: Make settings available to modules
    moduleName = models.CharField(max_length=32, blank=False, null=False)
    settingName = models.CharField(max_length=32, blank=False, null=False)
    settingValue = models.CharField(max_length=128, blank=True, null=True)

    @staticmethod
    def debug_print_module():
        frm = inspect.stack()[1]
        mod = inspect.getmodule(frm[0])
        return mod.__name__#.split(".")#[1]
