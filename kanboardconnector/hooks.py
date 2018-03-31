# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "kanboardconnector"
app_title = "KanboardConnector"
app_publisher = "libracore"
app_description = "Connector for ERPNext to Kanboard to import tasks"
app_icon = "fa fa-tasks"
app_color = "#4f4f4f"
app_email = "info@libracore.com"
app_license = "AGPL"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/kanboardconnector/css/kanboardconnector.css"
# app_include_js = "/assets/kanboardconnector/js/kanboardconnector.js"

# include js, css files in header of web template
# web_include_css = "/assets/kanboardconnector/css/kanboardconnector.css"
# web_include_js = "/assets/kanboardconnector/js/kanboardconnector.js"

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
# get_website_user_home_page = "kanboardconnector.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "kanboardconnector.install.before_install"
# after_install = "kanboardconnector.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "kanboardconnector.notifications.get_notification_config"

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

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"kanboardconnector.tasks.all"
# 	],
# 	"daily": [
# 		"kanboardconnector.tasks.daily"
# 	],
# 	"hourly": [
# 		"kanboardconnector.tasks.hourly"
# 	],
# 	"weekly": [
# 		"kanboardconnector.tasks.weekly"
# 	]
# 	"monthly": [
# 		"kanboardconnector.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "kanboardconnector.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "kanboardconnector.event.get_events"
# }

