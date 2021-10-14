import requests as re
file_list = re.get('http://cs7ns1.scss.tcd.ie?shortname=shelkem')
print(file_list.text)
filenames = re.get('http://cs7ns1.scss.tcd.ie/index.php?shortname=shelkem&download=noresume_speed')
print(filenames.text)
filedownload = re.get('http://cs7ns1.scss.tcd.ie/index.php?shortname=shelkem&myfilename=0023a1e023923e99d236ee999954868a1d41e5f7.png')
open('file1.png','wb').write(filedownload.content)