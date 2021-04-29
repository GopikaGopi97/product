from odoo import api,fields,models


class Hobbies(models.Model):
    _name = "hobby.list"
    _description = "hobbies"
    
    name=fields.Char(string="Name")
    hobbiefee_ids=fields.One2many('mark.list','hobby_id',string="Hobbiefee Id")