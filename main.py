import requests

response = requests.get("https://official-joke-api.appspot.com/random_joke")
joke = response.json()
print(f"Setup: {joke['setup']}")
print(f"Punchline: {joke['punchline']}")

print("This is the first version of the application")

print("This is the second version of the application")