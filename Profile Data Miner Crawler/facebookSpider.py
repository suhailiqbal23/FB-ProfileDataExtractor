import getpass
import time
import codecs
import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import settings as S
from spider.seleniumparse import SeleniumParse
from item.fbprofileitem import FacebookProfileItem
from url import urls1 as spiderurl

class FacebookSpider(object):
    '''
    classdocs
    '''
    def inputCredential(self):
        email="ENTER EMAIL HERE"
        password="ENTER PASSWORD HERE"
        return {'email':email,'password':password}
    
    def parseURL(self,userinfo):
        isFirst=True
        driver=webdriver.Firefox()
        sparse=SeleniumParse()
        fbProfileItems=[]
        
        if isFirst:
            driver.get("http://www.facebook.com")
            sparse.parseSource(sparse.loginFacebook(driver, userinfo),True)
        else:
            pass
        for u in spiderurl.URLs:
            driver.get(u[0])
            fbProfileItem=FacebookProfileItem()
            time.sleep(S.PAGE_TIME_INTERVAL)
            fbProfileItem=sparse.parseSource(driver,False)
            print (u[0])
            if fbProfileItem:
                setattr(fbProfileItem,'profile_url',u[0])
                fbProfileItems.append(fbProfileItem)
                
            self.writeCSV(fbProfileItems)
        driver.close()
    def writeCSV(self,fbProfileItems):
        with open('last.csv','a',newline='',encoding="utf-8") as fcsv:
            writer=csv.writer(fcsv)
           # writer.writerow(S.properties)
            for fb in fbProfileItems:
                fbProfileItem=[]
            for prop in S.properties:
                fbProfileItem.append(getattr(fb,str(prop)))
            writer.writerow(fbProfileItem)
        print ('*************Finished write csv file!**************')

if __name__ == '__main__':
    fbSpider=FacebookSpider()
    userinfo=fbSpider.inputCredential()
    print ('--------Spider Start----------')
    startTime=time.ctime()
    print(startTime)
    fbSpider.parseURL(userinfo)
    endTime=time.ctime()
    print ('--------Spider End----------')
    #print ('Total time cost:\t',(endTime-startTime))       
