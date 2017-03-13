from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from subprocess import call
import time, platform, sys#, win32api

filename = 'printer_output.pdf'#raw_input("file to print: ")#"printer_output.pdf"
os_plat = platform.system()

"""
pdf = canvas.Canvas("printer_output.pdf", pagesize=letter)
pdf.drawString(72, 720, time.ctime(time.time()))
pdf.drawString(72, 648, "@Mike Castellana")
pdf.drawString(72, 576, "Printing From Script Test")
pdf.save()
"""
pdf = canvas.Canvas("printer_output.pdf", pagesize=letter)
pdf.drawString(72, 720, time.ctime(time.time()))
y=648 #36
file = open('ise-out.txt', 'r')
for line in file.readlines():
	if line != '\n':
		line = str(line).replace('\n','')
		pdf.drawString(72, y, str(line))
	#print line
	y-=36
file.close
pdf.save()
#sys.exit(0)

printer_ip = "64.102.40.215"#raw_input("Printer IP: ")

if os_plat.lower() == 'darwin' or os_plat.lower() == 'linux':
	if os_plat.lower() == 'darwin': print "Running on Mac OS X"
	elif os_plat.lower() == 'linux':print "Running on MAC OS X" 
	IPP_addr = "https://"+printer_ip
	printer_name = "ISE_SCRIPT_PRINTER"
	print_name_arg = "-P"+printer_name
	
	#print "\nlpadmin", "-E", "-p", printer_name, "-v", IPP_addr, "-E"
	#print "lpr", print_name_arg, filename
	call(["lpadmin", "-E", "-p", printer_name, "-v", IPP_addr, "-E"])
	print "Initializing Printer..."
	time.sleep(2)
	call(["lpr", print_name_arg, filename])
	print "Printing..."
	time.sleep(2)
	call(["lpadmin", "-x", printer_name])
	print "Tearing down connection..."
	time.sleep(2)

elif os_plat.lower() == 'windows':
	print "Running on Windows"
	print_name_arg = "-S"+printer_name
	win32api.ShellExecute (["print https://64.102.40.215 filename"])
	win32api.ShellExecute (["lpr", print_name_arg, "-d", filename])

else:
	print "Incompatible OS -- application designed to work with Mac, Windows, or Linux based Kernels"
	print "Exiting..."
	sys.exit(0)
