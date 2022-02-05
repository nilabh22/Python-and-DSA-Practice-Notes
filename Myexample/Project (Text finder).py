import shutil
path = 'C:\\Users\\Nilabh Sahu\\PycharmProjects\\Myexample\\unzip_me_for_instructions'
shutil.unpack_archive('unzip_me_for_instructions.zip',path+'\\extracted_content','zip')
with open(path+'\\extracted_content\\Instructions.txt') as f :
    print(f.read())

import re
pattern = r'\d{3}-\d{3}-\d{4}'

def search(file,pattern = r'\d{3}-\d{3}-\d{4}'):
    f = open(file,'r')
    text = f.read()
    if re.findall(pattern,text):
        return re.findall(pattern,text)
    else:
        return ''

import os
result = []

for folders,sub_folders,files in os.walk(path+'\\extracted_content'):
    for f in files:
        full_path = folders+'\\'+f
        result.append(search(full_path))

for r in result:
    if r!= '':
        print(r)
    else:
        pass

