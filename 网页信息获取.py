import requests
def getHTMLText(url):
   try:
       r= requests.get(url, timeout=30)
       r.raise_for_status()#如果状态不是200，引发异常
       r.encoding ="utf-8" #无论原来用什么编码，都改成utf-8
       return r.text
   except:
       return""
url="http://www.lenove.com"
print(getHTMLText(url))
