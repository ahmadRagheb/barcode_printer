// Copyright (c) 2020, Abdullah Zaqout and contributors
// For license information, please see license.txt

frappe.ui.form.on('Barcode Printer', {
	refresh: function (frm) {
		$(cur_frm.$wrapper).find("button[data-fieldname='print']").removeClass("btn-xs btn-default").addClass("btn-primary").css({ 'min-width': '100%', 'font-size': '18px', 'margin-top': '18px' });
	},
	onload: function (frm) {
		frm.set_query("document_type", function () {
			return { filters: { name: ["in", ["Stock Entry", "Purchase Receipt"]] } };
		});
	},
	document_type: function (frm) {
		!frm.doc.document_type && frm.set_value("document", null)
	},
	document: function (frm) {
		frm.clear_table('items');
		frm.clear_table('serials_and_barcodes')
		frm.doc.document && cur_frm.events.fetchItems(frm)
		frm.refresh_field("items")
		frm.refresh_field("serials_and_barcodes")
	},
	fetchItems: function (frm) {
		frm.doc.list_of_items = []
		frappe.call({
			method: "frappe.client.get",
			args: {
				name: frm.doc.document,
				doctype: frm.doc.document_type
			},
			callback: function (r) {
				if (r.message) {
					r.message.items.forEach(row => {
						frm.add_child("items", {
							"item_code": row.item_code,
							"item_serial_no": row.serial_no || ""
						});

						row.serial_no && cur_frm.events.createBarcodes(frm, row.serial_no)
					});
					frm.refresh_field("items")
				}
			}
		});
	},
	createBarcodes: function (frm, serial_no) {
		serial_no.split("\n").forEach(element => {
			frm.add_child("serials_and_barcodes", {
				"barcode": element
			});
		});
		frm.refresh_field("serials_and_barcodes")
	},
	print: function (frm) {
		if (frm.doc.num <= 0 || !frm.doc.document) {
			frappe.throw("Missing Required Data!");
			return;
		}
		if (frm.is_dirty()) {
			frappe.throw('Please save form before print');
		}
		var w = window.open("/printview?doctype=Barcode Printer&name=" + cur_frm.doc.name + "&trigger_print=1&format=Barcode Print Format&no_letterhead=0&_lang=es");
		if (!w) {
			frappe.msgprint(__("Please enable pop-ups")); return;
		}
	}
});
