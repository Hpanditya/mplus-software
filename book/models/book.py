# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.datetime import datetime


class book(models.Model):
    _name = "book.book"

    name = fields.Char(
        string="Name",
        required=True,
    )

    author = fields.Char(
        string="Author",
        required=True,
    )

    

