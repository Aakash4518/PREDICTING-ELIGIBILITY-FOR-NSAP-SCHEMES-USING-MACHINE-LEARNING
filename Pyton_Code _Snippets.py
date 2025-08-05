import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account (https://au-syd.dai.cloud.ibm.com/docs/content/wsj/analyze-data/ml-authentication.html?context=cpdaas)
API_KEY = "<your API key>"
# API key is private so i dont' share it with here beacause anyone can use my API key furthure, so i dont want to share it.
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE:  manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [
	{
		"fields": [array_of_input_fields],
		"values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]
	}
]}

response_scoring = requests.post('https://private.au-syd.ml.cloud.ibm.com/ml/v4/deployments/2277dd73-3170-4327-8238-2d7c7db760fa/predictions?version=2021-05-01', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})

print("Scoring response")
try:
    print(response_scoring.json())
except ValueError:
    print(response_scoring.text)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
