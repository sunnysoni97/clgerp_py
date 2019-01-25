import StudClass
import DbManip
import Attendance
import MySQLdb

def getInfoStud():
	print "------------------------------------------------------------"
	print "Enter Name of the student : "
	name = raw_input()
	print "Enter DOB of the student : "
	dob = raw_input()
	print "Enter Address of the student : "
	addr = raw_input()
	print "Enter Phone Number of the student : "
	phone = raw_input()
	print "Enter Email-ID of the student : "
	mail = raw_input()
	print "Enter Department of the student : "
	dept = raw_input()
	print "Enter Batch of the student (passing year) : "
	batch = int(raw_input())
	s1 = StudClass.stud()
	s1.createNew(name,dob,addr,phone,mail,dept,batch)
	print "------------------------------------------------------------"
	return s1

def getInfoPar():
	print "------------------------------------------------------------"
	print "Enter Name of the Father : "
	pname = raw_input()
	print "Enter Phone Number of the Father : "
	pphone = raw_input()
	print "Enter Mail of the Father : "
	pmail = raw_input()
	p1 = StudClass.parent()
	p1.createNew(pname,pphone,pmail)
	print "------------------------------------------------------------"
	return p1

def displayStud(s):
	print "-------STUDENT DETAILS-------"
	print "Roll : %s" % (s.rollNo)
	print "Name : %s" % (s.name)
	print "DOB : %s" % (s.dob)
	print "Address : %s" % (s.addr)
	print "Phone : %s" % (s.phone)
	print "Email-ID : %s" % (s.mail)
	print "Department : %s" % (s.dept)
	print "Batch : %s" % (s.batch)
	print "------------------------------"

def displayPar(p):
	print "-------PARENT DETAILS---------"
	print "Name : %s" % (p.name)
	print "DOB : %s" % (p.phone)
	print "Email-ID : %s" % (p.mail)
	print "------------------------------"

