from odoo import api, fields, models

class CustomerDetails(models.Model):
    _name = "customer.order"
    _description = "Customer order Records"
    _rec_name = 'name'
      
    name = fields.Char(string='Customer Name')
   #  state=fields.Selection([('draft','Draft'), ('order','Order'),], default="draft",required="True",string="state")



   #  def confirm(self):
   #       if not self.name:
   #          raise Warning("name should be entered")
   #       else:
   #          self.state="order"
   