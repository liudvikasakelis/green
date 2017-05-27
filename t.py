#!/usr/bin/python

import sys
import l1
import csv

url = sys.argv[1]

url_list = l1.i_scraper(url)

print("Length ", len(url_list))

with open('test.csv', 'w') as csvfile:
    wr = csv.DictWriter(csvfile, 
                        fieldnames = ['url', 'first_name', 'last_name', 'email',
                                      'company_name', 'phone_number', 
                                      'fax_number', 'address1', 'address2',
                                      'city', 'zip', 'state', 'website',
                                      'category', 'description', 'facebook',
                                      'twitter', 'pinterest', 'linkedin'])
    wr.writeheader()
    counter = 1
    for url in url_list:
        wr.writerow(l1.scraper('http://www.greenpeople.org' + url))
        print(counter)
        counter = counter + 1 