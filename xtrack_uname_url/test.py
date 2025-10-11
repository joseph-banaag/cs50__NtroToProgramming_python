import re

email_pattern = r"([\w.-]+)@([\w.-]+)"
email_address = "user.name@example.com"

match = re.search(email_pattern, email_address)

if match:
    email_add = match.group(0)
    # email_add = match.groups() # this will display $ ('user.name', 'example.com')
    username = match.group(1)
    domain = match.group(2)
    print(f"User email address: {email_add}")
    print(f"Username: {username}")
    print(f"Domain: {domain}")
else:
    print("Email address not found.")