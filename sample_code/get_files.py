import requests as re
file_list = re.get('http://cs7ns1.scss.tcd.ie?shortname=shelkem')
print(file_list.text)
filenames = re.get('http://cs7ns1.scss.tcd.ie.index.php?download=noresume_speed&shortname=shelkem&myfilename=2122/shelkem/pi-project2/shelkem-challenge-filenames.csv')
print(filenames.text)