import requests
print(requests.__version__)

print(requests.get("https://google.ca"))
url = "https://raw.githubusercontent.com/CarterWP01/lab1/main/script.py"
res = requests.get(url)
print(res.text)
