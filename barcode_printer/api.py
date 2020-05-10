import frappe


def create_barcode(doc, method):
    if doc.docstatus == 1:
        return 
    else:
        if doc.barcode_label != doc.name:
            doc.barcode_label = doc.name
            doc.save()