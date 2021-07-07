
class AddressSpider(object):
    '''
    parse address for where he lived
    '''
    print("ADD")
    def parse_content(self,cmt_soup,fbProfileItem):
        
     
        livespan=cmt_soup.find('span',text=u'Current City and Home Town')
      
        
        if livespan:
            addresses=livespan.parent.find_next_sibling('ul')
            
            for address in addresses.find_all('div',class_='fsm fwn fcg'):
                addresstype=address.get_text().strip()
                addressinfo=address.find_previous_sibling('span').find('a',{'data-hovercard':not None}).get_text()
                if addresstype==u'Current city':
                    setattr(fbProfileItem,'current_city',addressinfo)
                    print ('Current city:\t',addressinfo)
                elif addresstype==u'Home Town':
                    setattr(fbProfileItem,'hometown',addressinfo)
                    print ('Hometown:\t',addressinfo)
                else:
                    pass        
