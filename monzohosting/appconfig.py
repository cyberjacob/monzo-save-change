#!/usr/bin/env python
# coding=utf-8

from django.apps import AppConfig


class AccountManagerAppconfig(AppConfig):
    def can_accept_webhook(self, webhook_type):
        return False

    def call_transaction_created_webhook(self, webhook):
        raise RuntimeError("Webhook run not configured")
