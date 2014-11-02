#! /usr/bin/env python

import requests
import sys
import json

fake = {}

# Person
gender = 'male'
res_format = 'json'
person_url = 'http://api.randomuser.me/?format={0}&gender={1}'.format(
    res_format, gender)
person_req = requests.get(person_url)

if person_req.status_code == 200:
    result = person_req.json()
    jperson = result['results'][0]['user']
else:
    print("Error contacting the Random Person API")
    sys.exit()

fake['name'] = jperson['name']
fake['location'] = jperson['location']
fake['username'] = jperson['username']
fake['password'] = jperson['salt']

# Email
email = '{0}@mailinator.com '.format(jperson['username'])
email_url = 'https://www.mailinator.com/inbox.jsp?to={0}'.format(
    jperson['username'])

fake['email'] = email
fake['email_url'] = email_url

# Output
print json.dumps(fake, sort_keys=True, indent=4, separators=(',', ': '))
