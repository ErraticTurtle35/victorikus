# -*- coding: utf-8 -*-

from odoo import models, fields


class WebsitePage(models.Model):
    _inherit = 'website.page'

    active = fields.Boolean(default=True)
