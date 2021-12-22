# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ogmAttendance(models.Model):
    _name = 'ogm.attendance'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Attendance Sheet'

    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                            default =lambda self: _('New'))
    attendance_date = fields.Date(string="Date")
    batch_id = fields.Many2one("ogm.batch", string="Batch No.")
    trainee_id = fields.One2many('ogm.trainee.att', 'attendance_id', string='Trainees')
    company_id = fields.Many2one('res.company', string='Company', index=True, default=lambda self: self.env.company.id)

    @api.model
    def create(self, vals):
        if not vals.get('name') or vals['name'] == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('ogm.record') or _('New')
        return super(ogmAttendance, self).create(vals)

    @api.onchange('batch_id')
    def action_create_attendance(self):
        if self.trainee_id:
            self.trainee_id = [(5, 0, 0)]
            # for rec in self.trainee_id:
            #     rec.unlink()
        if self.batch_id.trainee_id:
            for trainee in self.batch_id.trainee_id:
                self.trainee_id = [(0, 0, {'trainee_id': trainee.id, 'attendance_id': self.id})]
                # self.env['ogm.trainee.att'].create({'trainee_id': trainee.id, 'attendance_id': self.id})

