
# imported the requests library
import requests
import git
from git import Repo
from random import randrange, uniform
import os




file1 = "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Sub1.txt"
file2 = "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Sub2.txt"
  
# URL of the file to be downloaded is defined as file
r1 = requests.get(file1) # create HTTP response object
r2 = requests.get(file2)
# send a HTTP request to the server and save
# the HTTP response in a response object called r
with open("../file12.txt",'wb') as f:
  
    # Saving received content as a png file in
    # binary format
  
    # write the contents of the response (r.content)
    # to a new file in binary mode.
    f.write(r1.content)

with open("../file22.txt",'wb') as t:
  
    # Saving received content as a png file in
    # binary format
  
    # write the contents of the response (r.content)
    # to a new file in binary mode.
    t.write(r2.content)

f = open("../file22.txt", "a")
f.write(str(randrange(0, 10))+"\n")
# f.write(os.path.abspath(".."))
f.close()
repo = git.Repo(os.path.abspath(".."))
file12 = 'file12.txt'
file22 = 'file22.txt'

repo.index.add([file12 , file22])
# repo.index.add([file2])
repo.index.commit('added new config22')
print('commit successfully')

origin = repo.remote(name='origin')
existing_branch = repo.heads['main']
existing_branch.checkout()

origin.push()
print('push sucessfully')
