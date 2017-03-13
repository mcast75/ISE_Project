import requests, time
from string import letters, digits, printable
import datetime
from lxml import etree

user = 'sponsor'
pwd  = 'Csap1'
ip="198.18.133.27"


def chron_job():
	while(1):
		tme = datetime.datetime.now()
		# if str(tme)[17:19] == '59' and (str(tme)[20:23]) >= '999':
		# 	print "hit: "+str(tme)
		# 	time.sleep(.2)
		if str(tme)[18] == '9' and (str(tme)[20:23]) >= '999':
			print "hit [datetime]:\t"+str(tme)
			print "hit [convtime]:\t"+str(get_convert_time(tme))
			print
			time.sleep(.2)

def get_convert_time(datetime):
	abbrv = {'01':'jan', '02':'feb', '03':'mar', '04':'apr', '05':'may', '06':'jun', '07':'jul', '08':'aug', '09':'sep', '10':'oct', '11':'nov', '12':'dec'}
	dash = '-'
	dot = '.'
	space = ' '
	
	time_s = str(datetime)
	year = time_s[2:4]
	month = time_s[5:7]
	day = time_s[8:10]
	print int(time_s[11:13]) == 12
	if int(time_s[11:13]) == 12:
		print '2'
		hh = str(int(time_s[11:13]))
	elif int(time_s[11:13])%12 < 10:
		print '1'
		hh = '0'+str(int(time_s[11:13])%12)
	else:
		print '3'
		hh = str(int(time_s[11:13])%12)
	mm = time_s[14:16]
	ss = time_s[17:19]
	new_time= day+dash+abbrv[month]+dash+year+space+hh+dot+mm+dot+ss

	return new_time


#Disable warnings???
requests.packages.urllib3.disable_warnings()
def recent_guests(user, pwd, ip):
	id_list=[]
	url = "https://"+ip+":9060/ers/config/guestuser?filter=creationTime.STARTSW.10-mar-17"
	headers={
		'Accept': "application/vnd.com.cisco.ise.identity.guestuser.2.0+xml",
		'Content-Type': 'application/vnd.com.cisco.ise.identity.guestuser.2.0+xml'
	}
	print url
	response = requests.request("GET", url, auth=(user,pwd), headers=headers, verify=False)
	root = etree.fromstring(str(response.text))
	if int(root.attrib['total'])!= 0:
		print "Response:"
		print etree.tostring(root, pretty_print=True)
		print '\n'
	print
	print "Number of recent : "+ str(root.attrib['total'])
	for count in range (0, int(root.attrib['total'])):
		print str(count+1)+".\t"+"Guest: "+str(root[0][0].attrib['name'])
		print"\t"+str(root[0][0].tag)+" : "+str(root[0][0].attrib['id'])
		id_list.append(str(root[0][0].attrib['id']))
	return id_list

def guest_user_by_id(user, pwd, ip, id_list):
	for resource in id_list:
		url = "https://"+ip+":9060/ers/config/guestuser/"+resource
		headers={
			'Accept': "application/vnd.com.cisco.ise.identity.guestuser.2.0+xml",
			'Content-Type': 'application/vnd.com.cisco.ise.identity.guestuser.2.0+xml'
		}
		response = requests.request("GET", url, auth=(user,pwd), headers=headers, verify=False)
		root = etree.fromstring(str(response.text))
		print "\n\nResponse:\n"
		print etree.tostring(root, pretty_print=True)
		print
		print (root[3][4].tag, root[3][4].text)
		print (root[3][5].tag, root[3][5].text)
		print (root[3][0].tag, root[3][0].text)
		print '*************'
		print (root[3][1].tag, root[3][1].text)
		print '*************'


		# for child in root:
		# 	for grand in child:
		# 		print(grand.tag, grand.text)
		#print

		file = open('ise-out.txt', 'w')
		file.write(''+str(root[3][4].tag)+' : '+str(root[3][4].text)+'\n')
		file.write(''+str(root[3][5].tag)+' : '+str(root[3][5].text)+'\n\n')
		file.write(''+str(root[3][0].tag)+' : '+str(root[3][0].text)+'\n\n')
		file.write(''+str(root[5].tag)+' : '+str(root[5].text)+'\n')
		file.close()


		

def all_guest_users(user, pwd, ip):
	url = "https://"+ip+":9060/ers/config/guestuser/"
	headers={
		'Accept': "application/vnd.com.cisco.ise.identity.guestuser.2.0+xml",
		'Content-Type': 'application/vnd.com.cisco.ise.identity.guestuser.2.0+xml'
	}
	response = requests.request("GET", url, auth=(user,pwd), headers=headers, verify=False)
	root = etree.fromstring(str(response.text))
	print "\n\nResponse:\n"
	print etree.tostring(root, pretty_print=True)


def new_guest(user, pwd, ip):
	url = "https://"+ip+":9060/ers/config/guestuser"
	headers={
		'Accept': "application/vnd.com.cisco.ise.identity.guestuser.2.0+xml",
		'Content-Type': "application/vnd.com.cisco.ise.identity.guestuser.2.0+xml",
	}

	body=''
	file = open('post-ise.xml', 'r')
	for line in file.readlines():
		body+=str(line)
	file.close
	response = requests.request("POST", url, auth=(user,pwd), headers=headers, data=body, verify=False)



if __name__ == '__main__':
	print '\n\n\n========================================'
	print '|+++\t\t\t            +++|\n|+++      ISE SOFTWARE PROJECT      +++|'
	print '|+++\t\t\t            +++|'
	print '========================================\n\n'


	
	chron_job()
	#res_list = recent_guests(user, pwd, ip)
	#guest_user_by_id(user, pwd, ip, res_list)
	#all_guest_users(user, pwd, ip)
	#new_guest(user, pwd, ip)

