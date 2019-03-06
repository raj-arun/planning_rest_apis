# Oracle Planning Rest APIs
Sample Scripts for invoking Oracle Planning REST APIs using Python

### Purpose of the Script
  - Get the Current active Planning API Version
  - Get the Current active Migration API Version
  - Get the application name
  
### You will need the following details to get this working:
  - Access to Oracle EPM Instance (PBCS, EPBCS)
  - Python 3.5
  - URL to the Planning Instance
  - Domain Name
  - User Name
  - Provide all the details in a file in a json format (check the pbcsdetails.txt file)

### Dependencies
The following libraries are used in the script:
  - requests
  - json
  - ast
  - sys

### How to Execute the Script
  - Install Python and the necessary libraries needed
  - Place the pbcsdetails.txt file and the python script in the same directory
  - Open terminal (mac) / powershell (windows)
  - Type "python planningAPIs.py"
  
### References
You can find more details about the REST APIs [here](https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/get_rest_api_versions_for_planning.html) and [here](https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/get_applications.html) and finally [here](https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/getting_api_versions_for_lcm_apis.html)
