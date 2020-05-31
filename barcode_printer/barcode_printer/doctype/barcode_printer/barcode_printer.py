# -*- coding: utf-8 -*-
# Copyright (c) 2020, Abdullah Zaqout and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document
import barcode as barcode_lib
from barcode.writer import ImageWriter
from io import BytesIO
from frappe import get_all,get_site_path



class BarcodePrinter(Document):
	def generate_barcodes(self,doctype,docname):
		print("===========================")
		if doctype == "Stock Entry":
			barcodes = get_all(doctype + " Detail",fields=["serial_no"],
													filters={"parent":docname})
			print(barcodes)
			filtered_codes = filter_serial_no(barcodes)
			final_barcodes = save_get_getbarcodes(filtered_codes,doctype,docname)

			return final_barcodes

def filter_serial_no(barcodes):
	filtered_serials = []
	list_of_serials = [barcode.get('serial_no') for barcode in barcodes for serial_no in barcode.keys() ] 
	for serials in list_of_serials:
		filtered_serials += (serials.split("\n"))

	return filtered_serials

def save_get_getbarcodes(barcodes,doctype,docname):
	import os
	site = get_site_path()
	if not docname:
		docname = doctype
	path = """/barcodes/{doctype}/{docname}/
					""".format(doctype=doctype,docname=docname)
	storage = site + path
	barcodes_path_list = []
	code128 = barcode_lib.get_barcode_class('code128')
	for barcode in barcodes:
		filename = barcode+".png"
		
		filepath = os.path.join(get_site_path('public', 'files'), filename)
		if os.path.exists(filepath):
			barcodes_path_list.append(filepath.split('public/')[-1])
			continue

		with open(filepath, 'wb') as f:
			code128(barcode, writer=ImageWriter()).write(f)
			barcodes_path_list.append(filepath.split('public/')[-1])

	return barcodes_path_list
		