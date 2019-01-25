import StudClass
import MySQLdb

def newAdmission(s,p,con):
	com = """insert into students (name,dob,addr,phone,mail,dept,batch) values ('%s','%s','%s','%s','%s','%s','%d')""" % (s.name,s.dob,s.addr,s.phone,s.mail,s.dept,s.batch)
	com2 = """insert into parents (name, phone, mail) values ('%s','%s','%s')""" % (p.name,p.phone,p.mail)
	cursor = con.cursor()
	try:
		cursor.execute(com)
		cursor.execute(com2)
		con.commit()
		com = """select rollNo from students where name = '%s' and dob = '%s' and addr = '%s'""" % (s.name,s.dob,s.addr)
		cursor.execute(com)
		res = cursor.fetchone()[0]
		com2 = """update parents set rollNo='%s' where name='%s' and phone = '%s'""" % (res,p.name,p.phone)
		cursor.execute(com2)
		com = """insert into attendance (rollNo) values (%s)""" % (res)
		cursor.execute(com)
		con.commit()
		return res
	except:
		con.rollback()
		print "Writing New Data Failed - newAdmission()"
	finally:
		pass

def delAdmission(rollNo,con):
	res = 0;
	try:
		cursor = con.cursor()
		com = """select * from students where rollNo = %s""" % (str(rollNo))
		cursor.execute(com)
		if(cursor.rowcount == 0):
			return res
		com = """delete from students where rollNo = %s""" % (str(rollNo))
		cursor.execute(com)
		com = """delete from parents where rollNo = %s""" %(str(rollNo))
		cursor.execute(com)
		com = """delete from attendance where rollNo = %s""" %(str(rollNo))
		cursor.execute(com)
		con.commit()
		com = """select * from students where rollNo = %s""" % (str(rollNo))
		cursor.execute(com)
		if(cursor.rowcount == 0):
			res = 1;
	except:
		print "Deleting Data Failed - delAdmission()"
		con.rollback()
	finally:
		return res

def editAdmission(rollNo, tableNo, fieldName, newValue, con):
	res = 0
	cursor = con.cursor()
	if(tableNo==0):
		com = """update students set %s='%s' where rollNo='%s'""" % (fieldName,newValue,str(rollNo))
	elif(tableNo==1):
		com = """update parents set %s='%s' where rollNo='%s'""" % (fieldName,newValue,str(rollNo))
	else:
		return res
	try:
		cursor.execute(com)
		con.commit()
		res = 1;
	except:
		print "Editing Data Failed - editAdmission()"
		con.rollback()
	finally:
		return res

def searchAdmission(rollNo,con):
	res = StudClass.stud();
	cursor = con.cursor()
	com = """select * from students where rollNo = '%s'""" % (str(rollNo))
	try:
		cursor.execute(com)
		temp = cursor.fetchone()
		res.createNew(temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7])
		setattr(res,'rollNo',temp[0])
	except:
		print "Search Failed - searchAdmission()"
	finally:
		return res

def searchParent(rollNo,con):
	res = StudClass.parent();
	cursor = con.cursor()
	com = """select * from parents where rollNo = '%s'""" % (str(rollNo))
	try:
		cursor.execute(com)
		temp = cursor.fetchone()
		res.createNew(temp[1],temp[2],temp[3])
		setattr(res,'rollNo',temp[0])
	except:
		print "Search Failed - searchParent()"
	finally:
		return res

def listAllRollNo(con):
	cursor = con.cursor()
	com = "select rollNo from students"
	try:
		cursor.execute(com)
		res = cursor.fetchall()
		return res
	except:
		print "Listing Roll No Failed - listAllRollNo()"
		return 0