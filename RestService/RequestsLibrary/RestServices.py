import requests

# GET request
resp = requests.get('http://dummy.restapiexample.com/api/v1/employees')

if resp.status_code != 200:
    print("Error", resp)
else:
    for item in resp.json():
        # print(item)
        pass
