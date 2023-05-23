
# imported the requests library
import requests
import git
from git import Repo

# repo_url = "https://github.com/mostafasadeghifar/v2ray-config.git"
# local_path = "/home/masi/Desktop/test"
# repo = git.Repo.clone_from(repo_url,local_path)
# print('repo cloned')

# file1 = "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Sub1.txt"
# file2 = "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Sub2.txt"
  
# # URL of the file to be downloaded is defined as file
# r1 = requests.get(file1) # create HTTP response object
# r2 = requests.get(file2)
# # send a HTTP request to the server and save
# # the HTTP response in a response object called r
# with open("../file1.txt",'wb') as f:
  
#     # Saving received content as a png file in
#     # binary format
  
#     # write the contents of the response (r.content)
#     # to a new file in binary mode.
#     f.write(r1.content)

# with open("../file2.txt",'wb') as t:
  
#     # Saving received content as a png file in
#     # binary format
  
#     # write the contents of the response (r.content)
#     # to a new file in binary mode.
#     t.write(r2.content)

repo = git.Repo("/home/masi/Desktop/v2ray-config")
file1 = 'file1.txt'
file2 = 'file2.txt'

repo.index.add([file1 , file2])
# repo.index.add([file2])
repo.index.commit('added new config')
print('commit successfully')

origin = repo.remote(name='origin')
existing_branch = repo.heads['main']
existing_branch.checkout()

origin.push()
print('push sucessfully')
