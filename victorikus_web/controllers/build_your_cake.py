# -*- coding: utf-8 -*
import logging

from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import route, request

logger = logging.getLogger(__name__)


class BuildYourCakeController(CustomerPortal):
    @route(['/build-your-cake'], type='http', auth="public", website=True, methods=['GET'])
    def build_your_cake(self, **kw):
        logger.info("build_your_cake endpoint called")
        return request.render("victorikus_web.build_your_cake", {})
