
from src.pdf_password import PDF

""" Example """	
p = PDF('C://tmp/a.pdf', 'C://tmp/o.pdf')
p.random_password()
p.create()
