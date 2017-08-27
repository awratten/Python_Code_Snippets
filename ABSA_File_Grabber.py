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

		fname = fname[-1]
		fname = fname.replace('"', '')

		with open(str(num) + "_" + fname, 'wb') as f:
			f.write(r.content)
	except:
		print('error' + str(num))

// LAST FILE: "383_Window Film Training.pdf"
