import re

text = """
Mr. Anderson
Ms. Thareja
Mrs. Morris
Mr. Roy
Ms. Gandhi
Mrs. Modi
https://www.google.com
http://www.udemy.com
www.udacity.com
https://www.stackoverflow.com
http://www.djsce.ac.in
https://plus.google.com
rishit.grover@gmail.com
kapeesh.grover@yahoo.co.in
abhishek.shah@gmail.com
shahp98@gmail.com
demo_user@gmail.com
rolflmoa@yahoo.co.in
27777647
233*333*88
455-78-888
022-240-93836
02642*221*381
"""

# Regular expression patterns
name_pattern = re.compile(r"(Mr\.|Ms\.|Mrs\.)\s([A-Z][a-z]+)")
website_pattern = re.compile(r"(?:https?://)?(?:www\.)?([a-zA-Z0-9.-]+)\.(?:[a-z]{2,})")
email_pattern = re.compile(r"([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,})")
phone_pattern = re.compile(r"(\d{3}[-.*]\d{3}[-.*]\d{4})|\(?\d{3}\)?[-.*]\d{3}[-.*]\d{4}")

# Find names
names = re.findall(name_pattern, text)
print("Names of the User:", [name[1] for name in names])

# Find website names excluding http/s
websites = re.findall(website_pattern, text)
print("Website names excluding http/s:", [website[0] for website in websites])

# Find email IDs
emails = re.findall(email_pattern, text)
print("Identified email IDs:", [email[0] for email in emails])

# Find phone numbers
phones = re.findall(phone_pattern, text)
print("Identified phone numbers:", [phone[0] for phone in phones])
