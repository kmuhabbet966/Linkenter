from bs4 import BeautifulSoup
import requests
print("Welcome to linkenter")
a = input("Please enter a link:")
r = requests.get(a)
source = BeautifulSoup(r.content,"lxml")
print(source)

