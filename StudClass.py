class stud:
	def __init__(self):
		self.name = ""
		self.dob = ""
		self.addr = ""
		self.phone = ""
		self.mail = ""
		self.dept = ""
		self.batch = 0
		self.rollNo = 0
	def createNew(self,name,dob,addr,phone,mail,dept,batch):
		self.name = name
		self.dob = dob
		self.addr = addr
		self.phone = phone
		self.mail = mail
		self.dept = dept
		self.batch = batch

class parent:
	def __init__(self):
		self.name = ""
		self.phone = ""
		self.mail = ""
	def createNew(self,name,phone,mail):
		self.name = name
		self.phone = phone
		self.mail = mail
