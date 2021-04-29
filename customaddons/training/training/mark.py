from odoo import api, fields, models


class StudentDetails(models.Model):
    _name = "mark.list"
    _description = "Student marks"
    
    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    marks=fields.Integer(string='Marks')

    currency_id=fields.Many2one('res.currency',string="Currency")
    student_fees=fields.Monetary(string="Student Fees")
    total_fees=fields.Float(string="Total Fees")
    student_ids=fields.Many2many('student.training',string="Student id")
    hobby_id=fields.Many2one('hobby.list', string="hobby_id")