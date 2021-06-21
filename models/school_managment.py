from odoo import models, fields, api
class Students(models.Model):
    _name = 'school.managment'
    _description = 'This is a school managment system'
    name = fields.Char('Student Name')
    roll = fields.Char('Student Roll')
    address = fields.Char('Student Address')
    student_DOB = fields.Date('DOB of student')

