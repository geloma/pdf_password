# pdf_password
	Using PyPdf to set pdf's password
	
	from src.pdf_password import PDF
	
	Examples
	* Default password (1234)
	p = PDF('/tmp/notsec.pdf', '/tmp/output.pdf')
	pdf.create()

	* Given password
	p = PDF('/tmp/notsec.pdf', '/tmp/output.pdf', 'mypassword')
	pdf.create()

	*Default random password
	p = PDF('/tmp/notsec.pdf', '/tmp/output.pdf')
	p.random_password()
	p.create()


