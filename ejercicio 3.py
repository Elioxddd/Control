import requests
import json

def comment(n):
    response = requests.get('https://jsonplaceholder.typicode.com/comments')
    consulta = json.loads(response.text)
    diccionario = {'comentario' : consulta[n]['body']}
    return diccionario

print(comment(3))