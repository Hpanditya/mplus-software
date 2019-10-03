# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class Book(models.Model):
    _name = "book.book"

    name = fields.Char(
        string="Name",
        required=True,
    )

    author = fields.Char(
        string="Author",
        required=True,
    )

    date_published = fields.Date(
        string="Date Published",
        defult=fields.Date.today(),
    )

    number_of_pages = fields.Integer(
        string="Number of Pages",
        default=0,
    )

    book_type_id = fields.Many2one(
        comodel_name="book.type",
        string="Type of Book",
    )


class BookType(models.Model):
    _name = "book.type"

    name = fields.Char(
        string="Book Type",
    )

