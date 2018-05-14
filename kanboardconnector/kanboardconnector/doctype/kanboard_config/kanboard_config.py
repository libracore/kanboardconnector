# -*- coding: utf-8 -*-
# Copyright (c) 2018, libracore and contributors
# For license information, please see license.txt
#
# Reference documents:
#   https://docs.kanboard.org/en/latest/api/project_procedures.html
#   https://docs.kanboard.org/en/latest/api/task_procedures.html
#
# Execute with
#   bench execute kanboardconnector.kanboardconnector.doctype.kanboard_config.kanboard_config.sync
#

# import definitions
from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import json
import base64
try:
    from urllib import request as http
except ImportError:
    import urllib2 as http
from datetime import datetime

class KanboardConfig(Document):
    
	pass

# returns the auth header from the api token (string)
def get_auth_header(api_token):
    # authentication
    credentials = base64.b64encode('{}:{}'.format("jsonrpc", api_token).encode())
    auth_header_prefix = 'Basic ' 
    headers = {
        'Authorization': auth_header_prefix + credentials.decode(),
        'Content-Type': 'application/json',
    }
    return headers

# execute API function
def execute(host, api_token, payload):
    # request    
    request = http.Request(host, headers=get_auth_header(api_token), data=json.dumps(payload).encode())
    response = http.urlopen(request).read()

    body = json.loads(response.decode())
    return body['result']

# read all projects
# returns a list of dicts for each project
def get_projects(host, api_token):
    # parameters
    payload = {
        'jsonrpc': '2.0',
        'method': 'getAllProjects',
        'id': "{0}{1}{2}".format(datetime.utcnow().hour, datetime.utcnow().minute, datetime.utcnow().microsecond)
    }  
    return execute(host, api_token, payload)

# read tasks of a project
def get_tasks(host, api_token, project_id):
    # parameters
    payload = {
        'jsonrpc': '2.0',
        'method': 'getAllTasks',
        'id': "{0}{1}{2}".format(datetime.utcnow().hour, datetime.utcnow().minute, datetime.utcnow().microsecond),
        'params': {
            'project_id': project_id,
            'status_id': 1              # only read active tasks
        }
    }
    return execute(host, api_token, payload)

# read column definition (to parse status)
def get_columns(host, api_token, project_id):
    # parameters
    payload = {
        'jsonrpc': '2.0',
        'method': 'getColumns',
        'id': "{0}{1}{2}".format(datetime.utcnow().hour, datetime.utcnow().minute, datetime.utcnow().microsecond),
        'params': {
            'project_id': project_id
        }
    }
    return execute(host, api_token, payload)

@frappe.whitelist()
def sync():
    config = frappe.get_single("Kanboard Config")
    
    if config.token and config.host:
        # start sync
        # read all projects
        projects = get_projects(config.host, config.token)
        for project in projects:
            # only work on active projects
            if project['is_active'] == "1":
                # check if this project exists already
                erp_project = frappe.get_doc("Project", project['name'])
                if erp_project:
                    # project exists
                    
                else:
                    # project does not exist in ERPNext, create
                    new_project = frappe.get_doc({"doctype": "Project"})
                    new_project.project_name = project['name']
                    new_project.status = "Open"
                    new_project.insert()
                    
                print("---{0}---".format(project['name']))
                columns = get_columns(host, api_token, project['id'])
                tasks = get_tasks(host, api_token, project['id'])
                for task in tasks:
                    #print("{0}: mod {1}".format(task['title'], task['date_modification']))
                    modified = datetime.fromtimestamp(float(task['date_modification']))
                    for column in columns:
                        if column['id'] == task['column_id']:
                            status = column['position']
                            break
                    description = task['description']
                    print("{0}: {1} - {2} [{3}]".format(task['id'], task['title'].encode('utf-8'), modified, status))
                    
    else:
        frappe.log_error("Kanboard Connector: attempted sync, but configuration missing host or api token")
        return
    
