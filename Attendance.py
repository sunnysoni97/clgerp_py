import MySQLdb

def calc_attendance(dP,tD):
	return (dP/tD*100.0)

def updateAttendance(rollNo,month,percent,con):
	cursor = con.cursor()
	res=0
	com = """select * from attendance where rollNo='%s'""" % (rollNo)
	cursor.execute(com)
	if(cursor.rowcount==0):
		return res
	com = """update attendance set %s='%d' where rollNo='%s'""" % (month,percent,str(rollNo))
	try:
		cursor.execute(com)
		con.commit()
		res=1
	except:
		print "attendance update failed - updateAttendance()"
		con.rollback()
	finally:
		return res

def getAttendance(rollNo,month,con):
	cursor = con.cursor()
	com = """select %s from attendance where rollNo='%s'""" % (month,rollNo)
	res=0;
	try:
		cursor.execute(com)
		res = cursor.fetchone()[0]
		return res
	except:
		print "attendance fetching failed - getAttendance()"
	finally:
		return res
