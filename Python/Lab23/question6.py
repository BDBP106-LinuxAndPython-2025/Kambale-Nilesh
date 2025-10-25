# (6) Write a Python script that reads in a piece of text and prints it out masking out
# email addresses. Thus and email address ”helloworld@python.com” should become
# ”h********d@python.com”.
import re
text = input("Enter text: ")
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
def mask_email(match):
    email = match.group()
    name, domain = email.split('@')
    if len(name) <= 2:
        masked_name = name[0] + "*" * (len(name) - 1)
    else:
        masked_name = name[0] + "*" * (len(name) - 2) + name[-1]
    return masked_name + "@" + domain

masked_text = re.sub(pattern, mask_email, text)

print("\nMasked text:")
print(masked_text)
