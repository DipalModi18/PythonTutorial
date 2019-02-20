import requests
import json

session = requests.session()

response = session.post(
			"https://so-lab-ent1-sevone-metered-trial.silverpeak.cloud/gms/rest/authentication/login",
			data=json.dumps({"user": "dmohan@sevone.com", "password": "Silverpeak123!@#"}),
			headers={'Content-type': 'application/json'}, timeout=10)

print(str(response.headers))


str1='dipalamodi123'
print(str1[:10])