import requests, time, sys
import datetime
from lxml import etree

class ISE_Print:
	#Disable warnings???
	requests.packages.urllib3.disable_warnings()

	def chron_job(self):
		while(1):
			tme = datetime.datetime.now()
			# if str(tme)[17:19] == '59' and (str(tme)[20:23]) >= '999':
			# 	print "hit: "+str(tme)
			# 	time.sleep(.2)
			if str(tme)[18] == '9' and (str(tme)[20:23]) >= '999':
				#print "hit [datetime]:\t"+str(tme)
				#print "hit [convtime]:\t"+str(get_convert_time(tme))
				ret_str = str(self.get_convert_time(tme))[:15]
				time.sleep(.2)
				return ret_str

	def get_convert_time(self, datetime):
		abbrv = {'01':'jan', '02':'feb', '03':'mar', '04':'apr', '05':'may', '06':'jun', '07':'jul', '08':'aug', '09':'sep', '10':'oct', '11':'nov', '12':'dec'}
		dash = '-'
		dot = '.'
		space = ' '
		
		time_s = str(datetime)
		year = time_s[2:4]
		month = time_s[5:7]
		day = time_s[8:10]
		if int(time_s[11:13])+4 == 12:
			hh = str(int(time_s[11:13])+4)
		elif (int(time_s[11:13])+4)%12 < 10:
			hh = '0'+str((int(time_s[11:13])+4)%12)
		else:
			hh = str((int(time_s[11:13])+4)%12)
		mm = time_s[14:16]
		ss = time_s[17:19]
		new_time= day+dash+abbrv[month]+dash+year+space+hh+dot+mm+dot+ss

		return new_time

	def recent_guests(self, user, pwd, ip, tme):
		id_list=[]
		url = "https://"+ip+":9060/ers/config/guestuser?filter=creationTime.STARTSW."+tme
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

	def guest_user_by_id(self, user, pwd, ip, id_list):
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

	def all_guest_users(self, user, pwd, ip):
		url = "https://"+ip+":9060/ers/config/guestuser/"
		headers={
			'Accept': "application/vnd.com.cisco.ise.identity.guestuser.2.0+xml",
			'Content-Type': 'application/vnd.com.cisco.ise.identity.guestuser.2.0+xml'
		}
		response = requests.request("GET", url, auth=(user,pwd), headers=headers, verify=False)
		root = etree.fromstring(str(response.text))
		print "\n\nResponse:\n"
		print etree.tostring(root, pretty_print=True)

	def new_guest(self, user, pwd, ip):
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
		print response.text



# if __name__ == '__main__':
# 	print '\n\n\n========================================'
# 	print '|+++\t\t\t            +++|\n|+++      ISE SOFTWARE PROJECT      +++|'
# 	print '|+++\t\t\t            +++|'
# 	print '========================================\n\n'

# 	itr = 1
# 	all_guest_users(user, pwd, ip)
# 	#res_list=["70ee18e0-08e3-11e7-91d1-005056aa900c"]
# 	#guest_user_by_id(user, pwd, ip, res_list)
	
# 	while(1):
# 		try:
# 			print "Iteration: "+str(itr)
# 			tme = chron_job()
# 			print "chron: "+tme
# 			res_list = recent_guests(user, pwd, ip, tme)
# 			guest_user_by_id(user, pwd, ip, res_list)
# 			print "\n\n\n"
# 			if itr ==2:
# 				new_guest(user, pwd, ip)
# 			itr+=1

# 		except KeyboardInterrupt:
# 			print '\n\n\n********************************'
# 			print '***\t\t\t     ***\n***      Session Closed      ***'
# 			print '***\t\t\t     ***'
# 			print '********************************\n\n'
# 			sys.exit(0)
		

	
	#chron_job()
	#res_list = recent_guests(user, pwd, ip)
	#guest_user_by_id(user, pwd, ip, res_list)
	#all_guest_users(user, pwd, ip)
	#new_guest(user, pwd, ip)

