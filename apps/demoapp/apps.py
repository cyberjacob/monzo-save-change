#!/usr/bin/env python
# coding=utf-8

from monzohosting.appconfig import AccountManagerAppconfig
from monzohosting import models

class DemoappConfig(AccountManagerAppconfig):
    name = 'apps.demoapp'

    def can_accept_webhook(self, webhook_type):
        if webhook_type == "transaction.created":
            return True
        return super().can_accept_webhook(webhook_type)

    def call_transaction_created_webhook(self, webhook):
        models.Setting.get_monzo().create_feed_item(webhook["data"]["account_id"],
                                                     "transaction pushed",
                                                     "http://www.nyan.cat/cats/original.gif")
