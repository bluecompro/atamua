# -*- coding: utf-8 -*-
##############################################################################
#
#    @package t_print_voucher Print Account Invoice Odoo 8.0
#    @copyright Copyright (C) 2013 T.V.T Marine Automation (aka TVTMA). All rights reserved.#
#    @license http://www.gnu.org/licenses GNU Affero General Public License version 3 or later; see LICENSE.txt
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import fields, models

class res_currency(models.Model):
    _inherit = 'res.currency'
    
    lts_currency_text = fields.Char(string='Currency Text', size=256, translate=True, help="The full text of the currency, e.g. United State Dollar, Vietnam Dong, etc")