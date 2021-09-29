import json # to parse JSON
import requests # to make HTTP requests
import argparse # to parse command-line arguments
import sys

url1="https://api.github.com/users/emaadmanzoor/repos?page=1"
url2="https://api.github.com/users/emaadmanzoor/repos?page=2"
url3="https://api.github.com/users/emaadmanzoor/repos?page=3"
url4="https://api.github.com/users/emaadmanzoor/repos?page=4"

r1=requests.get(url1)
r2=requests.get(url2)
r3=requests.get(url3)
r4=requests.get(url4)

r1=r1.json()
r2=r2.json()
r3=r3.json()
r4=r4.json()

r=r1+r2+r3+r4

count=0

for i in r:
  count += i['stargazers_count']

print(count)
