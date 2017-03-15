import requests
from lxml import etree

requests.packages.urllib3.disable_warnings()

user = 'sponsor'
pwd  = 'Csap1'
ip="198.18.133.27"


url = "https://"+ip+":9060/ers/config/guestuser/"
headers={
	'Accept': "application/vnd.com.cisco.ise.identity.guestuser.2.0+xml",
	'Content-Type': 'application/vnd.com.cisco.ise.identity.guestuser.2.0+xml'
}
response = requests.request("GET", url, auth=(user,pwd), headers=headers, verify=False)
print response.text
root = etree.fromstring(str(response.text))
print "\n\nResponse:\n"
print etree.tostring(root, pretty_print=True)