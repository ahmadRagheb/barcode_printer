import frappe


def create_barcode(doc, method):
    if doc.docstatus == 1:
        return 
    else:
        if doc.barcode_label != doc.name:
            doc.barcode_label = doc.name
            doc.save()


def create_purchase_date(doc, method):
    for row in doc.items:
        purchase_date =""
        has_serial_no = frappe.get_value('Item', row.item_code, 'has_serial_no')	
        if has_serial_no:
            serial_no_list  = row.serial_no.splitlines()
            if len(serial_no_list)>0:
                for sno in serial_no_list:
                    purchase_document_type = frappe.get_value('Serial No', sno, 'purchase_document_type')
                    purchase_document_no = frappe.get_value('Serial No', sno, 'purchase_document_no')
                    if purchase_document_type == "Stock Entry":
                        se_doc = frappe.get_doc("Stock Entry",purchase_document_no)
                        for se in se_doc.items:
                            se_serial_no_list  = se.serial_no.splitlines()
                            new_se_list =[]
                            for ss in se_serial_no_list:
                                new_se_list.append(ss.upper())
                            if sno in new_se_list:
                                purchase_date = purchase_date + str(se.purchasing_date) + "\n"
        row.purchase_date = purchase_date
