import requests

response = requests.get('http://127.0.0.1:8001/todo/api/v1.0/tasks', headers={'Authorization': 'Token secret-token-1'})

print(response.text)