import shutil

with open('data.txt', 'r') as fr, open('g.txt', 'a') as fw:
     shutil.copyfileobj(fr, fw)
