import re
import requests
url=input()
r=requests.get(url)
email_regex=r'[\W\.-]+@[\w\.-]+'
contact_regex=r'(\+?\d?[- ]?)?(\()?(\d){3}(\))?[-. ]?(\d){3}[-.]?(\d){4})
link_regex=r'https?://(facebook|linkedin|twitter)\.com[\w\.]+'
print('Social links-')
for match in re.findall(link_regex,r.text):
print(match)

print('Email/s-')
for match in re.findall(email_regex,r.text):
print(match)
print('Contact:')
for match in re.findall(contact_regex,r.text):
print(match)