import re

text = "my email is ali@gmail.com and I live in Lahore"

match = re.search(r"[\w]+@[\w]+\.com", text)
print(match.group())  # ali@gmail.com