from http.client import HTTPSConnection
from urllib.parse import quote

class NaverNewsDAO:
    def getNews(self,searchTxt):
        q=quote(searchTxt)  
        h={"X-Naver-Client-Id" : "FN5LcznRqbcO34foOQjK","X-Naver-Client-Secret":"NExju9i_rd"}
        hc=HTTPSConnection("openapi.naver.com")
        hc.request("GET","/v1/search/news.xml?query="+q,headers=h)
        rb=hc.getresponse().read() 
        hc.close()
        return rb