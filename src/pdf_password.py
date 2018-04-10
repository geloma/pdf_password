import sys
import random
import string
from pyPdf import PdfFileWriter, PdfFileReader

class PDF(object):
	""" PDF Class """
	filename = ""
	outputname = ""
	password = ""
	
	def __init__(self, filename="", outputname="", passwd=None):
		""" Constructor """
		if filename == "":
			sys.exit("Filename not given")
		if outputname == "":
			sys.exit("Outputname not given")
		self.filename = filename
		self.outputname = outputname
		self.password = passwd
		if not passwd:
			self.password = "1234"
	
	def create(self):
		""" Create PDF """
		print "[+] The password is " + self.password
		writer = PdfFileWriter()
		input_pdf = PdfFileReader(file(self.filename, "rb"))
		for page in range(0, input_pdf.getNumPages()):
			writer.addPage(input_pdf.getPage(page))
		output_stream = file(self.outputname, "wb")
		writer.encrypt(self.password, use_128bit=True) #max security by lib
		writer.write(output_stream)
		output_stream.close()
		print "[+] Done"
		
	def random_password(self):
		""" Generate random password """
		pass_len = 10
		self.password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(pass_len))
	

