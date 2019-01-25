import DbManip
import StudClass
import Attendance
import ConFrontend
import MySQLdb

flag=1
choice=0
con = MySQLdb.connect("localhost","root","","clgmgmt",unix_socket='/opt/lampp/var/mysql/mysql.sock')
choice=0
while(flag):
	print "------------------------------"
	print "----------STUDENT-ERP---------"
	print "MAIN MENU : "
	print "1. Register a New Student"
	print "2. Edit an existing Student"
	print "3. Edit an existing Student (Parent) "
	print "4. Delete an existing Student"
	print "5. Search for an existing Student"
	print "6. Update a student's attendance"
	print "7. Fetch a student's attendance"
	print "8. Exit the program"
	print "Enter your choice : "
	choice = int(raw_input())
	if(choice==1):
		s1 = StudClass.stud()
		s1 = ConFrontend.getInfoStud()
		p1 = StudClass.parent()			
		p1 = ConFrontend.getInfoPar()
		res = DbManip.newAdmission(s1,p1,con)
		if(res==0):
			print "Seat Not Allocated"
		else:
			print "Congrats! Roll No. of the New Student : %d" % (res)
	elif(choice==2):
		srch=int(raw_input("Enter rollno. of the student to edit info : "))
		fieldName = raw_input("Enter name of the field to change : ")
		newValue = raw_input("Enter changed value : ")
		res = DbManip.editAdmission(srch,0,fieldName,newValue,con)
		if (res):
			print "Student info changed successfully"
		else:
			print "Error changing student info"
	elif(choice==3):
		srch=int(raw_input("Enter rollno. of the parent's child to edit info : "))
		fieldName = raw_input("Enter name of the field to change : ")
		newValue = raw_input("Enter changed value : ")
		res = DbManip.editAdmission(srch,1,fieldName,newValue,con)
		if (res):
			print "Parent info changed successfully"
		else:
			print "Error changing parent info"
	elif(choice==4):
		srch = int(raw_input("Enter rollno. of the student to delete : "))
		res = DbManip.delAdmission(srch,con)
		if(res):
			print "Student deleted!!!"
		else:
			print "Student Not Found"

	elif(choice==5):
		srch = int(raw_input("Enter rollno. of the student to search for : "))
		s1 = DbManip.searchAdmission(srch,con)
		p1 = DbManip.searchParent(srch,con)
		ConFrontend.displayStud(s1)
		ConFrontend.displayPar(p1)
	
	elif(choice==6):
		srch = int(raw_input("Enter rollno. of the student to update attendance : "))
		month = raw_input("Enter month to change info : ")
		td = int(raw_input("Enter percent of attendance : "))
		res = Attendance.updateAttendance(srch,month,td,con)
		if(res):
			print "Attendance UPdated!!!"
		else:
			print "Failed to update attendance!!!"
	elif(choice==7):
		srch = int(raw_input("Enter rollno.of the student to fetch attendance : "))
		srch2 = raw_input("Enter month : ")
		res = Attendance.getAttendance(srch,srch2,con)
		if(res!=0):
			print "Attendance of the student is : %d" % (res)
		else:
			print "Failed to get attendance!"
	elif(choice==8):
		flag=0
		print "Exiting Client"