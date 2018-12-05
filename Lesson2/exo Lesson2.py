######################## Performance financières des entreprises sur Reuters #######

# coding: utf-8
import requests
import unittest
from bs4 import BeautifulSoup
import urllib
from lxml import etree
from lxml import html
import requests
import urllib
import re   # regex


base = "https://www.reuters.com/finance/stocks/financial-highlights/"




def _handle_request_result_and_build_soup(request_result):
  if request_result.status_code == 200:
    html_doc =  request_result.text
    soup = BeautifulSoup(html_doc,"html.parser")
    return soup


def _convert_string_to_float(string):
    regex = re.compile(r'[\n\r\t]')
    s = regex.sub(" ", str(string))
    s=s.replace("€","")
    s=s.replace(",","")
    s=s.replace("(","")
    s=s.replace(")","")
    s=s.replace("%","")

    return float(s.strip())


def get_price_change_query(query):
    
    url=base+query
    res = requests.get(url)
    soup = _handle_request_result_and_build_soup(res)
    stock_class = {'style':'font-size: 23px;'}
    stock_price =soup.find("span",stock_class).text
    
    change_class={'class':'neg'}
    stock_change =soup.findAll("span",change_class)[1].text

    return {'stock_price':_convert_string_to_float(stock_price),'stock_change':_convert_string_to_float(stock_change)/100}


def get_quartermean (query):
    
    url=base+query
    res = requests.get(url)
    soup = _handle_request_result_and_build_soup(res)
    
    listetables=soup.findAll("tr", {'class':'stripe'})

    found=False
    k=0

    while( found==False and k < len(listetables) ):
        found=str(listetables[k]).find("Quarter") != -1
        k=k+1

    if found : 
        quarterlist=listetables[k-1]
        quartermean=quarterlist.findAll("td",{'class':'data'})[1].text
        
    return _convert_string_to_float(quartermean)




def get_shares_owned (query):
    
    url=base+query
    res = requests.get(url)
    soup = _handle_request_result_and_build_soup(res)
    
    listetables=soup.findAll("tr", {'class':'stripe'})

    found=False
    k=0

    while( found==False and k < len(listetables) ):
        found=str(listetables[k]).find("Shares Owned") != -1
        k=k+1

    if found : 
        shareslist=listetables[k-1]
        shares_owned=shareslist.findAll("td",{})[1].text
        
    return _convert_string_to_float(shares_owned)






def get_dividends (query):
    
    url=base+query
    res = requests.get(url)
    soup = _handle_request_result_and_build_soup(res)
    
    listetables=soup.findAll("tr", {'class':'stripe'})

    found=False
    k=0

    while( found==False and k < len(listetables) ):
        found=str(listetables[k]).find("Dividend Yield") != -1
        k=k+1

    if found : 
        dividendlist=listetables[k-1]
        dividend=list(map(lambda x:x.text,dividendlist.findAll("td",{})[1:4]))
        
    return  {'divcompany':_convert_string_to_float(dividend[0]) , 'divindustry':_convert_string_to_float(dividend[1]) ,'divsector':_convert_string_to_float(dividend[2]) ,}


def getfirmstat(query):
    return{'stock_price':get_price_change_query(query)['stock_price'],'stock_change':get_price_change_query(query)['stock_change'] ,"Quarter Mean":get_quartermean (query),
     'Shares_owned':get_shares_owned(query),  'divcompany': get_dividends (query)['divcompany'] , 'divindustry': get_dividends (query)['divindustry'] 
     , 'divsector': get_dividends (query)['divsector'] }


#class reutersTests(unittest.TestCase):
   # def testdividends(self):
    #    self.assertEqual(get_dividends("LVMH.PA") , {'divcompany': 1.82, 'divindustry': 1.67, 'divsector': 2.15})

        
lvmh = getfirmstat("LVMH.PA")
print("LVMH  : " , lvmh)
airbus=getfirmstat("AIR.PA")
print("AIRBUS : " , airbus)
danone=getfirmstat("DANO.PA")
print("Danone : " , danone)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
