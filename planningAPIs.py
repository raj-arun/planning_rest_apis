import requests
import json
import sys
import ast
from requests.auth import HTTPBasicAuth

headers = {'Content-Type':'application/json'}

def get_login_details():
	with open("pbcsdetails.txt","r") as file:
		line = ast.literal_eval(file.read())
		domain_name = (line['domain'])
		user_name = domain_name + '.' + (line['login'])
		password = (line['pwd'])
		instance_url = (line['url'])
		return(domain_name,user_name,password,instance_url)

def get_application_details():
	'''
		Get the Application Name from the instance
		Input: None
		Output: application name
	'''
	response = requests.get(rest_end_point,auth=HTTPBasicAuth(uname,password),headers = headers)
	if response.status_code == 200:
		json_data = json.loads(response.text)
		for d in json_data["items"]:
			print("Application Name : ", d['name'])

def get_planning_api_version():
	'''
		Get the latest planning api version
		Input: None
		Output: planning api version
	'''
	response = requests.get(planning_url,auth=HTTPBasicAuth(uname,password),headers = headers)
	if response.status_code == 200:
		version_data = json.loads(response.text)
		for v in version_data["items"]:
			if(v['isLatest']):
				api_version = v['version']
	return(api_version)

def get_migration_api_version():
	'''
		Get the latest migration api version
		Input: None
		Output: migration api version
	'''
	response = requests.get(migration_url,auth=HTTPBasicAuth(uname,password),headers = headers)
	if response.status_code == 200:
		version_data = json.loads(response.text)
		for v in version_data["items"]:
			if(v['latest']):
				api_version = v['version']
	return(api_version)

domain_name, uname, password, instance_url = get_login_details()

planning_url =  instance_url + '/HyperionPlanning/rest/'
migration_url = instance_url + '/interop/rest/'

planning_api_version = get_planning_api_version()	

rest_end_point = instance_url + '/HyperionPlanning/rest/' + planning_api_version + '/applications'

get_application_details()

migration_api_version = get_migration_api_version()	
		
print('Planning API Version : ',planning_api_version)
print('Migration API Version : ',migration_api_version)




