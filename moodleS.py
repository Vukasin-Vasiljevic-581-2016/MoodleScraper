#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import smtplib
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import requests
from bs4 import BeautifulSoup
from lxml import html
import html2text

# Fill in your details here to be posted to the login form.
payload = {
    'username': 'yourUsername',
    'password': 'yourPassword'
}

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post('logInPage', data=payload)

    # An authorised request.
    r = s.get('pageYouWantToInspect')

# Parse through the string 
soup = BeautifulSoup(r.text, 'html.parser')

# Finding right section
	# By html inspection on web page 
section = soup.find(id='idNumberHere') #or class='' etc..

section_text = section.get_text()

string = "StringToCompare"

# Test to see if anything changed
if section_text == section6:
	print("Nothing changed!")
	pass

else:
	# If something changed send me email
	print("success")
	server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("youremail@gmail.com", "yourPassword")
        msg="MessageHere"
        server.sendmail("youremail@gmail.com","recieversemail@gmail.com", msg)
        server.quit()



