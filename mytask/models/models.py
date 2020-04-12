from PIL.ImageChops import difference

from odoo import api, fields, models
from odoo.osv.expression import select_distinct_from_where_not_null, select_from_where


class stock_move(models.Model):

    _inherit = 'stock.move'
    weight = fields.Float(string="weight")
    diff=fields.Float("The Difference",compute="_compute_difference",readonly=True,default=0.0)

    def _compute_difference(self):
        if(self.weight!=0):
            self.diff = self.product_uom_qty - self.weight
        else:
            self.diff=0.0

        if(self.diff<0):
            self.diff=0.0
