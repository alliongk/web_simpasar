# -*- coding: utf-8 -*-

from odoo import models, fields, api


class web_simpasar(models.Model):
    _name = 'web.simpasar'
    _description = 'Web Simpasar'

    name = fields.Char(string='Name')
    

