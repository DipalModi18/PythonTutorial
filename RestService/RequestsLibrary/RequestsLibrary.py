import requests
from requests.exceptions import HTTPError


#
#
# The GET method indicates that you are trying to get or retrieve data from a specified resource.
# To make a GET request, invoke requests.get().
response = requests.get('https://api.github.com')


#
#
print(response.status_code)  # Return value of get() is an instance of Response
responseDict = response.json()  # To get a dictionary
print('Response as a dictionary: ' + str(responseDict))
# To know the metadata about the response, you will need to look at the response’s headers.
print('Headers: ' + str(response.headers))


#
#
for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()  # When you want to raise an exception if the request was unsuccessful.
        # If you invoke.raise_for_status(), an HTTPError will be raised for certain status codes.
        # If the status code indicates a successful request,
        # 	the program will proceed without that exception being raised.
    except HTTPError as http_err:
        print('HTTP error occurred: ' + str(http_err))
    except Exception as err:
        print('Other error occurred: ' + str(err))
    else:
        # In Python, using the else statement,
        # you can instruct a program to execute a certain block of code only in the absence of exceptions.
        print('Success!')


#
#
# To pass values through query string parameters in the URL using get(), you pass data to params.
# Search GitHub's repositories for requests
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)
print(response.json())

# You can pass params to get() in the form of a dictionary, as you have just done, or as a list of tuples
response = requests.get(
        'https://api.github.com/search/repositories',
        params=[('q', 'requests+language:python')],
    )
print(response.json())

# To customize headers, you pass a dictionary of HTTP headers to get() using the headers parameter.
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)
print(response.json())


#
#
# Aside from GET, other popular HTTP methods include POST, PUT, DELETE, HEAD, PATCH, and OPTIONS.
# requests provides a method, with a similar signature to get(), for each of these HTTP methods
response = requests.post('https://httpbin.org/post', data={'key': 'value'})
# data takes a dictionary, a list of tuples, bytes, or a file-like object.
response = requests.put('https://httpbin.org/put', data={'key': 'value'})
response = requests.delete('https://httpbin.org/delete')
response = requests.head('https://httpbin.org/get')
response = requests.patch('https://httpbin.org/patch', data={'key': 'value'})
response = requests.options('https://httpbin.org/get')

# If, however, you need to send JSON data, you can use the json parameter.
# When you pass JSON data via json, requests will serialize your data and add the correct Content-Type header for you.
response = requests.post('https://httpbin.org/post', json={'key': 'value'})


# httpbin.org is a great resource created by the author of requests, Kenneth Reitz.
# It is a service that accepts test requests and responds with data about the requests.

