from datetime import time
from plyer import notification
import requests
from bs4 import BeautifulSoup


def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,
        timeout=15
    )

def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    # notifyMe("ARPIT!!", "LETS STOP THE SPREAD OF THIS VIRUS TOGETHER")

    myHtmlData = getData('https://www.mohfw.gov.in/')

    soup = BeautifulSoup(myHtmlData, 'html.parser')
    # print(soup.prettify())

    myDataStr = " "
    for tr in soup.find_all('tbody')[1].find_all('tr'):
        myDataStr += tr.get_text()

    print(myDataStr)
    myDataStr = myDataStr[1:]
    itemList = myDataStr.split("\n\n")

    states = ['Chandigarh']
    for item in itemList[0:21]:
        dataList = item.split('\n')

        if dataList[1] in states:
            nTitle = 'Cases of Covid-19'
            nText = f"State {dataList[1]}\nIndian : {dataList[2]} & Foreign : {dataList[3]}\n Cured : {dataList[4]}\n Deaths : {dataList[5]}"
            notifyMe(nTitle, nText)
    #         time.sleep(2)
    # time.sleep(3600)
