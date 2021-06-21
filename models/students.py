from odoo import models, fields, api
class Students(models.Model):
    _name = 'students'
    _description = 'This is students of school managment system'
    name = fields.Char('Student Name')
    roll = fields.Char('Student Roll')
    address = fields.Char('Student Address')
    student_DOB = fields.Date('DOB of student')