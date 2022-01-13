# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class trainee(models.Model):
    _name = 'ogm.trainee'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Trainee Record'

    name = fields.Char(string='Name', required=True)
    trainee_age = fields.Integer('Age', required=True)
    trainee_number = fields.Integer('Number', required=True)
    batch_id = fields.Many2one("ogm.batch", string="Batch No.", required=True)

    @api.constrains('trainee_number')
    def _check_trainee_number(self):
        if len(str(abs(self.trainee_number))) != 6:
            raise ValidationError(_('trainee number must be only 6 digits'))


class batch(models.Model):
    _name = 'ogm.batch'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Trainee Batches'

    name = fields.Char(string='Batch Number', required=True)
    batch_description = fields.Selection([('electrical', 'Electrical'), ('scaffolding', 'Scaffolding'),
                                          ('welding', 'Welding'), ('pipefitting', 'Pipefitting'),
                                          ('instrumentation', 'Instrumentation'),
                                          ('safety', 'Safety')], string="Batch Description")
    trainee_id = fields.One2many('ogm.trainee', 'batch_id', string='Trainees')
    # task_id = fields.Many2one('ogm.task', 'Task')


class task(models.Model):
    _name = 'ogm.task'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Trainer Tasks'

    name = fields.Char(string='Title')
    assigned_to = fields.Many2one('res.users', 'Trainer')
    batch_id = fields.Many2one('ogm.batch', 'Batch')
    task_date = fields.Date(string="Date")
    task_time = fields.Datetime(string="Task Time")
    task_stop = fields.Datetime(string="Task Ends")
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancelled')], default='draft', string="Status")

    # def write(self, vals):
    #     print("vals", vals)
    #     print("***************************", self.batch_id)
    #
    #     if 'batch_id' in vals:
    #         print('new batch id =', vals['batch_id'])
    #         if vals['batch_id']:
    #             b = self.env['ogm.batch'].search([('id', '=', vals['batch_id'])])
    #             b.write({'task_id': self.id})
    #
    #
    #     res = super(task, self).write(vals)
    #
    #     return res

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
