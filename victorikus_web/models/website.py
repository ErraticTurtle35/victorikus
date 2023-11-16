# -*- coding: utf-8 -*-

from odoo import models, api, SUPERUSER_ID, fields


class Website(models.Model):
    _inherit = 'website'

    active = fields.Boolean(default=True)
