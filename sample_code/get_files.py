import requests as re
file_list = re.get('http://cs7ns1.scss.tcd.ie?shortname=shelkem')
print(file_list.text)
filenames = re.get('http://cs7ns1.scss.tcd.ie/index.php?shortname=shelkem&download=noresume_speed')
print(filenames.text)