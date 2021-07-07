
class BasicInfoSpider(object):
    '''
    Parse person basic information
    '''
    print("INFO")
    def parse_content(self,cmt_soup,fbProfileItem):
        
        basicdiv=cmt_soup.find('div',{'id':'pagelet_basic'})
        if basicdiv:
            self.get_basic_info(basicdiv,fbProfileItem)
        
        contactdiv=cmt_soup.find('div',{'id':'pagelet_contact'})
        if contactdiv:
            self.get_contact_info(contactdiv, fbProfileItem)
            

        socialdiv=cmt_soup.find('span',text=u'Websites and social links')
        if socialdiv is None:
            return
       
        if socialdiv:
           
         socialul= socialdiv.parent.find_next_sibling('ul')
       
        for socialli in socialul:
            infotype=socialli.div.div.span.get_text().strip()            
            infocontent=socialli.div.div.find_next_sibling('div').span.get_text().strip()
            
            if infotype=='Social links':
                setattr(fbProfileItem,'','social_links')
                setattr(fbProfileItem,'social_links',infocontent)
                print ('Social links:\t',infocontent)
        
            
    def get_basic_info(self,info_soup,fbProfileItem):
        basicul=info_soup.find('ul')
        if basicul.find('span',text='No basic info to show'):
            return
        for basicli in basicul:
            infotype=basicli.div.div.span.get_text().strip()            
            infocontent=basicli.div.div.find_next_sibling('div').span.get_text().strip()            
            self.parse_basic_info(infotype, infocontent,fbProfileItem)      
    
    def get_contact_info(self,info_soup,fbProfileItem):
        
        contactul=info_soup.find('ul')
        print(contactul)
        if contactul.find('span',text='No contact info to show'):
         return
        for contactli in contactul:
            infotype=contactli.div.div.span.get_text().strip()            
            infocontent=contactli.div.div.find_next_sibling('div').span.get_text().strip()            
            self.parse_contact_info(infotype, infocontent,fbProfileItem)      
    
    def parse_basic_info(self,infotype,infocontent,fbProfileItem):
        if infotype=='Gender':
            setattr(fbProfileItem,'gender',infocontent)
            print ('Gender:\t',infocontent)
        elif infotype=='Languages':
            setattr(fbProfileItem,'language',infocontent)
            print ('Languages:\t',infocontent)
        elif infotype=='Religious views':
            setattr(fbProfileItem,'relegious_views',infocontent)
            print ('Religious views:\t',infocontent)
        elif infotype=='Political Views':
            setattr(fbProfileItem,'political_views',infocontent)
            print ('Political Views:\t',infocontent)     
        elif infotype=='Birthday':
            
                setattr(fbProfileItem,'birth_date',infocontent)
                print ('Birth Date:\t',infocontent)
                
    def parse_contact_info(self,infotype,infocontent,fbProfileItem):
        '''if infotype=='Websites':
            setattr(fbProfileItem,'screen_name','Website')
            setattr(fbProfileItem,'website',infocontent)
            print ('Website:\t',infocontent)
        elif infotype=='Facebook':
            setattr(fbProfileItem,'screen_name','Facebook')
            setattr(fbProfileItem,'website',infocontent)
            print ('Facebook:\t',infocontent)'''
        if infotype=='Mobile phones':
            setattr(fbProfileItem,'','phone')
            setattr(fbProfileItem,'phone',infocontent)
            print ('Mobile phones:\t',infocontent)
        elif infotype=='Email address':
            setattr(fbProfileItem,'','email')
            setattr(fbProfileItem,'email',infocontent)
            print ('Email address:\t',infocontent)
        
        else:
            pass

    
