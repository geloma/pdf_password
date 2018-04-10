""" Examples """
from src.pdf_password import PDF

# Default password (1234)
p = PDF('/tmp/notsec.pdf', '/tmp/output.pdf')
pdf.create()

# Random password
p = PDF('C://tmp/a.pdf', 'C://tmp/o.pdf')
p.random_password()
p.create()

# Given password
p = PDF('/tmp/notsec.pdf', '/tmp/output.pdf', 'mypassword')
pdf.create()

