import requests, requests.utils
import re
# import PyPDF2

url = "https://www.absa.net.au/documents/item/"

for num in range(999):
	# num = 251
	try:
		r = requests.get(url + str(num))

		d = r.headers['content-disposition']
		fname = re.findall("filename=(.+)", d)

		fname = fname[-1] # Extract Filename string from list
		fname = fname.replace('"', '') # Remove " from filename string

		with open(str(num) + "_" + fname, 'wb') as f: # add document number to original filename
			f.write(r.content)
	except:
		print('Error_' + str(num)) # print error message if no file is found

# LAST FILE: "383_Window Film Training.pdf"
