# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "barcode_printer"
app_title = "Barcode Printer"
app_publisher = "Abdullah Zaqout"
app_description = "Barcode Printer App To Print Serial No. as Barcode"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "zaqoutabed@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/barcode_printer/css/barcode_printer.css"
# app_include_js = "/assets/barcode_printer/js/barcode_printer.js"

# include js, css files in header of web template
# web_include_css = "/assets/barcode_printer/css/barcode_printer.css"
# web_include_js = "/assets/barcode_printer/js/barcode_printer.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "barcode_printer.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "barcode_printer.install.before_install"
# after_install = "barcode_printer.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "barcode_printer.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

doc_events = {
	"Delivery Note": {
		"on_update": "barcode_printer.api.create_barcode",
		# "on_cancel": "method",
		# "on_trash": "method"
	}
}


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"barcode_printer.tasks.all"
# 	],
# 	"daily": [
# 		"barcode_printer.tasks.daily"
# 	],
# 	"hourly": [
# 		"barcode_printer.tasks.hourly"
# 	],
# 	"weekly": [
# 		"barcode_printer.tasks.weekly"
# 	]
# 	"monthly": [
# 		"barcode_printer.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "barcode_printer.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "barcode_printer.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "barcode_printer.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


fixtures = [
    {
        "dt": "Print Format",
        "filters": [["doc_type", "in", ("Barcode Printer")]]
    },
	{"dt":"Custom Field", "filters": [["dt", "in", ("barcode_label")]]}
]