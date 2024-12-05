#
#& API ---> Application programming interface 

#& SOAP   XML

#& REST Trasnferencia de estado representacional 
#? JSON

import json
import requests

# #response = requests.get("http://numbersapi.com/42?json")
# #response = requests.get("http://numbersapi.com/5/math?json")
# response = requests.get("http://numbersapi.com/12/28/date?json")

# trivia = json.loads(response.content)

# print(trivia)
# print(json.dumps(trivia, indent=4))

# print(type(trivia))

# print(f"Trivia: {trivia['text']}")
# print(f"Number: {trivia['number']}")

# url = "https://catfact.ninja/fact"
# response = requests.get(url)
# if response.status_code == 200:
#     data = response.json()
#     print(f"Curiosidad sobre gatos: {data['fact']}")
# else:
#     print("Error al conectar con la API.")


# import json
# import requests

# #response = requests.get("http://numbersapi.com/42?json")
# #response = requests.get("http://numbersapi.com/5/math?json")
# response = requests.get("http://numbersapi.com/12/28/date?json")

# trivia = json.loads(response.content)

# print(trivia)
# print(json.dumps(trivia, indent=4))

# print(type(trivia))

# print(f"Trivia: {trivia['text']}")
# print(f"Number: {trivia['number']}")

# url = "https://catfact.ninja/fact"
# response = requests.get(url)
# if response.status_code == 200:
#     data = response.json()
#     print(f"Curiosidad sobre gatos: {data['fact']}")
# else:
#     print("Error al conectar con la API.")

import tkinter as tk
import requests
import json

def fetch_trivia():
    
    response = requests.get("http://numbersapi.com/5?json")
    
  
    if response.status_code == 200:
     
        trivia = response.json()
        trivia_label.config(text=trivia['text'])
    else:
        trivia_label.config(text="Error al obtener la trivia")

root = tk.Tk()
root.title("NumbersAPI")

fetch_button = tk.Button(root, text="Get Trivia", command=fetch_trivia)
fetch_button.pack(pady=20)
trivia_label = tk.Label(root, text="", wraplength=300)
trivia_label.pack(pady=20)

root.mainloop()
