import requests
import ApiError


# GET request
resp = requests.get('http://dummy.restapiexample.com/api/v1/employees')

if resp.status_code != 200:
    print("Error", resp)
else:
    for item in resp.json():
        # print(item)
        pass


# resp = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22%27+newark+%27%2C%20%27+de+%27%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys')
weather_response = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22%27+newark+%27%2C%20%27+de+%27%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys')

print(weather_response.json())
# try:
#     details = {"name": "testd", "salary": "123", "age": "23"}
#     resp = requests.post("http://dummy.restapiexample.com/api/v1/create", json=details)
# except:
#     print("Error encountered while POST request: ", ApiError("Api call failed"))
# else:
#     print("Employee created successfully")
