import unittest
from SI507project5_code import *
import os
import csv
import json


class testAPI(unittest.TestCase):
    def setUp(self):
        self.username='Abel0828'
        main(self.username)
    def test_output_filename(self):
        self.assertTrue(os.path.exists('followings.csv'))
        self.assertTrue(os.path.exists('followers.csv'))
    def test_followings_content(self):    
        if os.path.exists('followings.csv'):
            with open('followings.csv','r',encoding='utf-8') as f:
                reader=csv.DictReader(f,delimiter=',', quotechar = '"')
                count=0
                for row in reader:
                    count+=1
                    self.assertTrue(len(row)>1,'test column #')
                self.assertEqual(count,5)
    def test_followers_content(self): 
        if os.path.exists('followers.csv'):                    
            with open('followers.csv','r',encoding='utf-8') as f:
                reader=csv.DictReader(f,delimiter=',', quotechar = '"')
                count=0
                for row in reader:              
                    self.assertTrue(len(row)>1,'test column #')
                    count+=1
                self.assertEqual(count,1)
    

    def test_data_cache(self):
        self.assertTrue(os.path.exists('cache_contents.json'),'test data cache')
        if os.path.exists('cache_contents.json'):
            with open('cache_contents.json','r',encoding='utf-8') as f:
                data=json.load(f)
                for _,record in data.items():
                    if 'errors' not in record:        
                        self.assertEqual(record['expire_in_days'],0.5,'test expire days')

    def test_creds_cache(self):
        self.assertTrue(os.path.exists('creds.json'),'test cred cache')
        if os.path.exists('creds.json'):
            with open('creds.json','r',encoding='utf-8') as f:
                data=json.load(f)
                self.assertTrue('TUMBLR' in data,'test cred cache')
                if 'TUMBLR' in data:
                    self.assertTrue('values' in data['TUMBLR'],'test cred cache')
                    self.assertTrue(len(data['TUMBLR']['values'])>=1,'test cred cache')






if __name__ == "__main__":
    unittest.main(verbosity=2)
