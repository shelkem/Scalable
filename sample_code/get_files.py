import requests as re
file_list = re.get('http://cs7ns1.scss.tcd.ie?shortname=shelkem')
print(file_list.text)
filenames = re.get('index.php?download=noresume_speed&shortname=shelkem')
print(filenames.text)