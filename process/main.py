
# imported the requests library
import requests
import git
from git import Repo
from random import randrange, uniform
import os


# f = open("../file22.txt", "a")
# f.write(str(randrange(0, 10))+"\n")
# f.write(os.path.abspath("..")+"\n")
# f.close()

file1 = "https://raw.githubusercontent.com/AzadNetCH/Clash/main/V2Ray.txt"
  
# URL of the file to be downloaded is defined as file
r1 = requests.get(file1) # create HTTP response object

# send a HTTP request to the server and save
# the HTTP response in a response object called r j
# with open("/var/www/python/v2ray-config/config_file.txt",'wb') as f:
with open("../config_file.txt",'wb') as f:

    # Saving received content as a png file in
    # binary format
  
    # write the contents of the response (r.content)
    # to a new file in binary mode.
    f.write(r1.content)

# with open("../file22.txt",'wb') as t:
  
#     # Saving received content as a png file in
#     # binary format
  
#     # write the contents of the response (r.content)
#     # to a new file in binary mode.
#     t.write(r2.content)

f = open("../config_file.txt", "a")
f.write(str(randrange(0, 10))+"\n")
# f.write(os.path.abspath(".."))
f.close()
# repo = git.Repo("/var/www/python/v2ray-config")
# config = '/var/www/python/v2ray-config/config_file.txt'
# # file22 = 'file22.txt'

# repo.index.add([config])
# # repo.index.add([file2])
# repo.index.commit('added new configss')
# print('commit successfully')

# origin = repo.remote(name='origin')
# existing_branch = repo.heads['main']
# existing_branch.checkout()

# origin.push()
# print('push sucessfully')
