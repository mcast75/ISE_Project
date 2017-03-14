import ISE_Print

if __name__ == '__main__':
	print '\n\n\n========================================'
	print '|+++\t\t\t            +++|\n|+++      ISE SOFTWARE PROJECT      +++|'
	print '|+++\t\t\t            +++|'
	print '========================================\n\n'

	user = 'sponsor'
	pwd  = 'Csap1'
	ip="198.18.133.27"


	itr = 1
	ISE_Print.ISE_Print().all_guest_users(user, pwd, ip)
	#res_list=["70ee18e0-08e3-11e7-91d1-005056aa900c"]
	#guest_user_by_id(user, pwd, ip, res_list)
	
	while(1):
		try:
			print "Iteration: "+str(itr)
			tme = ISE_Print.ISE_Print().chron_job()
			print "chron: "+tme
			res_list = ISE_Print.ISE_Print().recent_guests(user, pwd, ip, tme)
			ISE_print.guest_user_by_id(user, pwd, ip, res_list)
			print "\n\n\n"
			if itr ==2:
				ISE_Print.ISE_Print().new_guest(user, pwd, ip)
			itr+=1

		except KeyboardInterrupt:
			print '\n\n\n********************************'
			print '***\t\t\t     ***\n***      Session Closed      ***'
			print '***\t\t\t     ***'
			print '********************************\n\n'
			sys.exit(0)
		

	
	#chron_job()
	#res_list = recent_guests(user, pwd, ip)
	#guest_user_by_id(user, pwd, ip, res_list)
	#all_guest_users(user, pwd, ip)
	#new_guest(user, pwd, ip)

