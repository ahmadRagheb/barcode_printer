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
		// frappe.call({
		// 	doc:frm.doc,
		// 	method:"generate_barcodes",
		// 	args:{
		// 		"doctype":frm.doc.document_type,
		// 		"docname":frm.doc.document
		// 	},
		// 	callback:function(result){
		// 		if(result.message){
		// 			let barcode_html = "";
		// 			result.message.forEach(barcode => {
		// 				barcode_html+=(`<img src="${barcode}" style="width:200px"/><br/>`)
		// 			});
		// 			frm.set_value("barcodes",barcode_html);
		// 			console.log(result.message);
		// 		}
		// 	}
		// })
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
						if (row.serial_no){
							var c = -1
							row.serial_no.split("\n").forEach(function (element, index) {
								let row = frm.add_child("serials_and_barcodes", {
									"barcode": element
								})
								frm.refresh_field("serials_and_barcodes")
								c = c+1
								cur_frm.grids[1].grid.grid_rows[index].toggle_view(true);

							});
							// frappe.model.set_value(row.doctype, row.name, "barcode",row.barcode_data); 
							console.log(c,"cc");
							cur_frm.grids[1].grid.grid_rows[c].toggle_view(false);

							frm.refresh_field("serials_and_barcodes")
						};
							
						
						// row.serial_no && cur_frm.events.createBarcodes(frm, row.serial_no)
					});
					frm.refresh_field("items")
				}
			}
		});
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


// frappe.ui.form.on('Serials And Barcodes', {
// 	barcode_data(frm,cdt, cdn) {
// 		print('xxxxxxxxxx')
// 			let row = frappe.get_doc(cdt, cdn);
// 			print(row)
	
// 		frappe.model.set_value(row.doctype, row.name, "barcode",row.barcode_data); 
// 		frm.refresh_field("serials_and_barcodes")

// 				// your code here
// 	}
// })