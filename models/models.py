# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class trainee(models.Model):
    _name = 'ogm.trainee'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Trainee Record'

    name = fields.Char(string='Name', required=True)
    trainee_age = fields.Integer('Age')
    batch_id = fields.Many2one("ogm.batch", string="Batch No.")


class batch(models.Model):
    _name = 'ogm.batch'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Trainee Batches'

    name = fields.Char(string='Batch Number', required=True)
    trainee_id = fields.One2many('ogm.trainee', 'batch_id', string='Trainees')


class task(models.Model):
    _name = 'ogm.task'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Trainer Tasks'

    name = fields.Char(string='Title')
    assigned_to = fields.Many2one('res.users', 'Trainer')
    task_date = fields.Date(string="Date")
    task_time = fields.Datetime(string="Task Time")
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancelled')], default='draft', string="Status")

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'


class traineeAttendance(models.Model):
    _name = 'ogm.trainee.att'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Trainee Record'

    trainee_id = fields.Many2one("ogm.trainee", string="Trainee")
    attendance_id = fields.Many2one("ogm.attendance", string="Attendance Ref.")
    Attended = fields.Boolean('Attended', default=False)
    note = fields.Text(string="Remark")
