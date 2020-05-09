import frappe


def create_barcode(doc, method):
    if doc.barcode_label != doc.name:
        doc.barcode_label = doc.name
        doc.save()