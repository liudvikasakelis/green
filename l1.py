#!/usr/bin/python3

import requests
from lxml import html


def i_scraper(url):
    try:
        page = requests.get(url)
    except requests.exceptions.ConnectionError:
        return 0
    
    tree = html.fromstring(page.content)
    
    results = tree.xpath('//td[@class="llistrowstyle"]/a/@href')
    
    return results 


def scraper(url):
    field_names = ['url', 'first_name', 'last_name', 'email', 
                   'company_name', 'phone_number', 'fax_number', 'address1', 
                   'address2', 'city', 'zip', 'state', 'website', 'category', 
                   'description', 'facebook', 'twitter', 'pinterest', 
                   'linkedin']
    
    xpath_q = {'first_name':'//doink',
               'last_name':'//doink',
               'email':'//doink',
               'company_name':'//h1/text()',
               'phone_number':'//doink',
               'fax_number':'//doink' ,
               'address1':'//td[div="Address:"]/../td[2]/div/b/text()',
               'address2':'//doink' ,
               'city':'//td[contains(text(), "City")]/../td[2]/b[1]/text()',
               'state':'//td[contains(text(), "City")]/../td[2]/b[2]/text()' ,
               'zip':'//td[contains(text(), "City")]/../td[2]/b[3]/text()',
               'state':'//td[contains(text(), "City")]/../td[2]/b[2]/text()' ,
               'website':'//td[div="WebSite:"]/../td[2]/b/text()',
               'category':'//doink' ,
               'description':'//doink' ,
               'facebook':'//doink' ,
               'twitter':'//doink' ,
               'pinterest':'//doink' ,
               'linkedin':'//doink' }
    
    results = {}
    results['url'] = url 
    
    try:
        page = requests.get(url)
    except requests.exceptions.ConnectionError:
        return 0
        
    tree = html.fromstring(page.content)
    
    for item in xpath_q.keys():
        try:
            results[item] = tree.xpath(xpath_q[item])[0]
        except IndexError:
            results[item] = None
            
    return(results)