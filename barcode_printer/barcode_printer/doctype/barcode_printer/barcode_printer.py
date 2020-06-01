# -*- coding: utf-8 -*-
# Copyright (c) 2020, Abdullah Zaqout and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document
from barcode import EAN13
from barcode.writer import ImageWriter
import base64


class BarcodePrinter(Document):
	def generate_barcodes(self):
		items = self.get("items")
		filtered_codes = filter_serial_no(items)
		final_barcodes = write_images(filtered_codes)
		return final_barcodes

def filter_serial_no(items):
	filtered_serials = []
	list_of_serials = [barcode.get('item_serial_no') for barcode in items ] 
	for serials in list_of_serials:
		filtered_serials += (serials.split("\n"))
	return filtered_serials

def write_images(filtered_codes):
	from io import BytesIO
	import barcode
	from barcode.writer import ImageWriter
	import base64
	CODE39 = barcode.get_barcode_class('code39')
	images = []
	for barcode in filtered_codes:
		# print to a file-like object:
		rv = BytesIO()
		CODE39(str(barcode), writer=ImageWriter()).write(rv)
		img_str = base64.b64encode(rv.getvalue()).decode()
		images.append(img_str)
		# rv.seek(0)
		rv.close()
	return images
