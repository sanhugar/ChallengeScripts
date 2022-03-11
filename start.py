# Import the needed credential and management objects from the libraries.
from azure.identity import ClientSecretCredential
import os
import sys
import json
def start_tests(credentials, subscription, args):

	inputs = json.loads(args)
	result = {}
	result['totalTests'] = ""
	result['failedTests'] = ""
	result['ignoredTests'] = ""
	result['outputFilePath'] = ""
	result['courseId'] = inputs["CourseId"]
	result['userId'] = inputs["UserId"]
	result['challengeId'] = inputs["ChallengeId"]
	result['labId'] = inputs["LabId"]
	result['attemptId'] = inputs["AttemptId"]
	result['error'] = ""
	result['testDetails'] = ""
	
	import challenge
	output = challenge.start_tests(credentials, subscription, args)
	import challenge2
	output2 = challenge2.start_tests(credentials, subscription, args)
	result['totalTests'] = output["totalTests"] + output2["totalTests"]
	result['failedTests'] = output["failedTests"] + output2["failedTests"]
	result['ignoredTests'] = output["ignoredTests"] + output2["ignoredTests"]
	jsonStr = json.dumps(result)
	return jsonStr