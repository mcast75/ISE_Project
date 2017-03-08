import requests
import base64
from requests.auth import HTTPBasicAuth
from basicauth import encode

uname,passwrd='ers-admin', 'Csap17'

encode_str=encode(uname, passwrd)
print encode_str.replace('Basic ','')
print 'ZXJzLWFkbWluOkNzYXAxNw=='

#Disable warnings???
requests.packages.urllib3.disable_warnings()

ip="198.18.133.27:9060"
url = "https://"+ip+"/ers/config/guestuser/"
headers={
	'Authorization': encode_str,
	'Accept': "application/vnd.com.cisco.ise.identity.guestuser.2.0+xml",
	#'content-type': 'application/vnd.com.cisco.ise.identity.guestuser.2.0+xml'
}
response = requests.request("GET", url, headers=headers, verify=False)
print response
