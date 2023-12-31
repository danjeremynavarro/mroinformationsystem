from . import __version__ as app_version

app_name = "mro_information_system"
app_title = "Mro Information System"
app_publisher = "Dan Navarro"
app_description = "For apps tailored specifically to the IT team in MRO"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "danjeremynavarro@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mro_information_system/css/mro_information_system.css"
# app_include_js = "/assets/mro_information_system/js/mro_information_system.js"

# include js, css files in header of web template
# web_include_css = "/assets/mro_information_system/css/mro_information_system.css"
# web_include_js = "/assets/mro_information_system/js/mro_information_system.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "mro_information_system/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "mro_information_system.install.before_install"
# after_install = "mro_information_system.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "mro_information_system.uninstall.before_uninstall"
# after_uninstall = "mro_information_system.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mro_information_system.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"mro_information_system.tasks.all"
#	],
#	"daily": [
#		"mro_information_system.tasks.daily"
#	],
#	"hourly": [
#		"mro_information_system.tasks.hourly"
#	],
#	"weekly": [
#		"mro_information_system.tasks.weekly"
#	]
#	"monthly": [
#		"mro_information_system.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "mro_information_system.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "mro_information_system.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "mro_information_system.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Request Events
# ----------------
# before_request = ["mro_information_system.utils.before_request"]
# after_request = ["mro_information_system.utils.after_request"]

# Job Events
# ----------
# before_job = ["mro_information_system.utils.before_job"]
# after_job = ["mro_information_system.utils.after_job"]

# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"mro_information_system.auth.validate"
# ]

