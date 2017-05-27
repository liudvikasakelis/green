#!/usr/bin/python3

import requests

def scraper(url):
    results = [None] * 10
    results[0] = url 
    try:
        page = requests.get(url)
    except requests.exceptions.ConnectionError:
        return 0
        
    tree = html.fromstring(page.content)
    
    
    
    return(results)