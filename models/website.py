from odoo import models, fields, api 

class BlogPost(models.Model):
    _inherit = 'blog.post'

    image = fields.Binary("Image")
    description = fields.Text("Description")