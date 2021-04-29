from odoo import api, fields, models

class ProductDetails(models.Model):
    _name = "product.sale"
    _description = "Product order Records"

    
    name= fields.Char(string='Product name')
    price=fields.Float(string="Price")
    currency_id=fields.Many2one('res.currency',string="Currency")
   