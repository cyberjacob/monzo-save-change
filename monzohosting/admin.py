#!/usr/bin/env python
# coding=utf-8

from django.contrib import admin
from monzohosting import models

admin.site.register(models.Settings, admin.ModelAdmin)
