#Azure challenge lab evaluation script
#Load required module references here
import sys
import json
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.compute.models import DiskCreateOption


testDetails = ""
error_msg = ""

def test_results(result, function):
	global testDetails
	if result:
		test_msg = function + "<b> Pass </b>"
	else:
		test_msg = function + "<b> Fail </b>"

	testDetails += test_msg + "<br>"

# this session is created with the region mentioned in the catalog. Make sure it is matching with the region given in the Challenge
def start_tests(credentials, subscriptionId, args):
	#args is a JSON as below example
	#args = '{"UserId":"umesh", "ChallengeId":"1", "AttemptId": "1", "WebhookUrl":"https://webhook.site/45183c1e-361d-4224-93e3-a439e22e845a", "CourseId":"5","LabId":"6", "Email":"UCB@nuvepro.com"}'	
	inputs = json.loads(args)

	totalTests = 0
	totalPass = 0
	# 
	# tests starting here

	# these are dependent of the Challenge and may need to change from one challenge to another challenge
	region = "eastus2"
	instanceName = inputs["VMName"]
	vmType = "Standard_B2ms"
	status = "running"
	
	

	totalTests += 1
	result = test_check_vm(credentials, subscriptionId, instanceName, region, vmType)
	totalPass += result
	test_results(result, "Checking if vm name is " + instanceName + " type is " + vmType + \
			" region is " + region)

	

	# tests ending here
	#

	result = {}
	result['totalTests'] = totalTests
	result['failedTests'] = totalTests - totalPass
	result['ignoredTests'] = 0
	result['outputFilePath'] = ""
	result['courseId'] = inputs["CourseId"]
	result['userId'] = inputs["UserId"]
	result['challengeId'] = inputs["ChallengeId"]
	result['labId'] = inputs["LabId"]
	result['attemptId'] = inputs["AttemptId"]
	result['error'] = error_msg
	result['testDetails'] = testDetails
	
	
	# converting to json string
	#jsonStr = json.dumps(result)
	#print("total pass: ",totalPass)
	#print("total tests: ",totalTests)    
	# returning the JSON data
	#return jsonStr
	return result

#
# All test functions starting from here
#
def test_check_vm(credentials, subscriptionId, instanceName, region, vmType):
	global error_msg
	try:
		# Retrieve the list of resource groups
		#group_list = credentials.resource_groups.list()
		#resource_client = ResourceManagementClient(credentials, subscriptionId)
		compute_client = ComputeManagementClient(credentials, subscriptionId)

		#groups = resource_client.resource_groups.list()
		#for group in groups:
			#print(group.name)
		vms = compute_client.virtual_machines.list_all()
		for vm in vms:
			hardware_profile = vm.hardware_profile
			if instanceName in vm.name:
				if region in vm.location: 
					if hardware_profile.vm_size in vmType:
						return 1
			
		
		return 0               

	except Exception as e:
		error_msg += str(e)
		return 0
   