import requests

header = {}
header['Authorization'] = "Token 4cc0075e86e46a4615b51b29ab5d476a3065f9b9"

r = requests.get('http://localhost:8000/rest-auth/user/', headers=header)
print(r.text)
