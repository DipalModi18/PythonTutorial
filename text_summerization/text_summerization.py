# import unirest
import requests

# response = unirest.post("http://httpbin.org/post", headers={ "Accept": "application/json" }, params={ "parameter": 23, "foo": "bar" })
response = requests.post(url="https://textanalysis-text-summarization.p.mashape.com/text-summarizer",
                         headers={
                             "X-Mashape-Authorization": "M81",
                             "Content-Type": "application/json"
                         },
                         params="{\"url\":\"http:\/\/en.wikipedia.org\/wiki\/Automatic_summarization\",\"text\":\"\",\"sentnum\":8}")


print(response.json())

