from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from subprocess import call
import time, platform, sys#, win32api

filename = raw_input("file to print: ")#"printer_output.pdf"
os_plat = platform.system()

"""
pdf = canvas.Canvas("printer_output.pdf", pagesize=letter)
pdf.drawString(72, 720, time.ctime(time.time()))
pdf.drawString(72, 648, "@Mike Castellana")
pdf.drawString(72, 576, "Printing From Script Test")
pdf.save()
"""

printer_ip = "64.102.40.215"#raw_input("Printer IP: ")

if os_plat.lower() == 'darwin' or os_plat.lower() == 'linux':
	if os_plat.lower() == 'darwin': print "Running on Mac OS X"
	elif os_plat.lower() == 'linux':print "Running on MAC OS X" 
	# IPP_addr = "https://"+printer_ip
	# printer_name = "ISE_SCRIPT_PRINTER"
	# print_name_arg = "-P"+printer_name
	
	# call(["lpadmin", "-E", "-p", printer_name, "-v", IPP_addr, "-E"])
	# call(["lpr", print_name_arg, filename])
	# call(["lpadmin", "-x", printer_name])

elif os_plat.lower() == 'windows':
	print "Running on Windows"
	print_name_arg = "-S"+printer_name
	win32api.ShellExecute (["print https://64.102.40.215 filename"])
	win32api.ShellExecute (["lpr", print_name_arg, "-d", filename])



else:
	print "Incompatible OS -- application designed to work with Mac, Windows, or Linux based Kernels"
	print "Exiting..."
	sys.exit(0)
