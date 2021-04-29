from odoo import api, fields, models

class SaleDetails(models.Model):
    _name = "sale.records"
    _description = "Sale Records"

    
    name_id=fields.Many2one('customer.order',string="Name")
    date=fields.Date(string='Date', default=lambda s: fields.Date.context_today(s))
    state = fields.Selection([('draft', 'Draft'),('confirm', 'Confirm'),], default="draft", string="status")
    
    sale_orderline_ids=fields.One2many('sale.orderline','reference_id')
    price_total = fields.Float(string="pricetotal", compute="_compute_price_total")

    def confirm(self):
        if not self.name_id:
            raise Warning("Name should be entered")
        else:
            self.state = "confirm"

    @api.depends('sale_orderline_ids','sale_orderline_ids.subtotal')
    def _compute_price_total(self):
        for rec in self:
            total = 0.0
            for rec1 in rec.sale_orderline_ids:
                total += rec1.subtotal
            rec.price_total = total



class SalesOrder(models.Model):
    _name="sale.orderline"
    _description="Order Line"

    reference_id = fields.Many2one('sale.records',string="reference")
    product_id=fields.Many2one('product.sale',string="Order Line")
    price=fields.Integer(string="Price")
    quantity=fields.Float(string="Quantity")
    subtotal=fields.Float(string="Subtotal")

    @api.onchange('price', 'quantity')
    def _compute_price(self):
        for rec in self:
            sub_total = 0
            if rec.price and rec.quantity:
                sub_total += (rec.quantity * rec.price)
                rec.subtotal = sub_total

    @api.onchange('product_id')
    def _compute_listprice(self):
        for rec in self:
            if rec.product_id:
                rec.price = rec.product_id.price