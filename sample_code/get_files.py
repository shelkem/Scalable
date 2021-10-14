import requests as re
# file_list = re.get('http://cs7ns1.scss.tcd.ie?shortname=shelkem')
filenames = re.get('http://cs7ns1.scss.tcd.ie/index.php?shortname=shelkem&download=noresume_speed')
filenames = filenames.text.split(',\n')
for each_file in filenames:
    filedownload = re.get('http://cs7ns1.scss.tcd.ie/index.php?shortname=shelkem&&download=noresume_speed&myfilename='+each_file)
    file = open(each_file, 'wb')
    file.write(filedownload.content)
    file.close()

