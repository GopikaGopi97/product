from odoo import api, fields, models


class StudentTraining(models.Model):
    _name = "student.training"
    _description = "Trainee Details"
    
    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    contact_no = fields.Char(string='Contact Number')
    address=fields.Char(string='Address')
    student_id=fields.Integer(string='Student id')
    is_employee=fields.Boolean(string='Current Employee')
    result=fields.Float(string='Result')
    date=fields.Datetime(string='Date')
    hobby_ids=fields.Many2many('hobby.list', 'stud_hobby_rel',string="Hobby ids")