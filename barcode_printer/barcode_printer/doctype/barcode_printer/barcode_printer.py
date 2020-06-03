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
		final_barcodes = write_images(filtered_codes, self)
		return final_barcodes

def filter_serial_no(items):
	filtered_serials = []
	list_of_serials = [barcode.get('item_serial_no') for barcode in items ] 
	for serials in list_of_serials:
		filtered_serials += (serials.split("\n"))
	return filtered_serials

def write_images(filtered_codes, doc):
	from io import BytesIO
	import barcode
	from barcode.writer import ImageWriter
	import base64
	from barcode import generate

	# module_width:	The width of one barcode module in mm as float. Defaults to 0.2.
	# module_height:	The height of the barcode modules in mm as float. Defaults to 15.0.
	# quiet_zone:	Distance on the left and on the right from the border to the first (last) barcode module in mm as float.
	#  Defaults to 6.5.
	# font_path:	Path to the font file to be used. Defaults to DejaVuSansMono (which is bundled with this package).
	# font_size:	Font size of the text under the barcode in pt as integer. Defaults to 10.
	# text_distance:	Distance between the barcode and the text under it in mm as float. Defaults to 5.0.
	# background:	The background color of the created barcode as string. Defaults to white.
	# foreground:	The foreground and text color of the created barcode as string. Defaults to black.

	CODE128 = barcode.get_barcode_class('code128')
	images = []
	for sno in filtered_codes:
		# print to a file-like object:
		rv = BytesIO()
		writerx=ImageWriter()
		writer_options = {"module_width": doc.module_width,
						"module_height": doc.module_height,
						"font_size": doc.font_size ,
						"text_distance": doc.text_distance,
						"quiet_zone": doc.quiet_zone}

		generate('code128', str(sno), writer=writerx, output=rv, writer_options=writer_options,text=None)

		img_str = base64.b64encode(rv.getvalue()).decode()
		images.append(img_str)
		rv.close()
	return images


