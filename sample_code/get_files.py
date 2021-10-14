import requests as re
file_list = re.get('http://cs7ns1.scss.tcd.ie',params={'shortname':'shelkem'})
print(file_list)