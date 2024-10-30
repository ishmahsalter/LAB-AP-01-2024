import re

User = "2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57"

pola = r'\A[a-zA-Z02468]{40}[13579\s]{5}\Z'

valid = re.match(pola, User) is not None

print('True' if len(User) == 45 and valid else 'False')
