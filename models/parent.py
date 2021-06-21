from odoo import models, fields, api
class Students(models.Model):
    _name = 'parent'
    _description = 'This is a parent sub_menu of configuration of school managment system'
    name = fields.Char('Student Name')
    roll = fields.Char('Student Roll')
    address = fields.Char('Student Address')
    student_DOB = fields.Date('DOB of student')