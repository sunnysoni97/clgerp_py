This is the reader's manual for using and editing this software project as you may like.

Prerequisites before using this software :

1. Make sure you have Python 2.x setup on your operating system.
2. Install the follow libraries to meet the dependencies :
	(i) MySQLdb (MySQL connector for python)
3. Install the MySQL server using any of the public distribuitions (XAMPP is recommended).
4. Import the database into your SQL server using the sql import file given in the repository (ClgMgmt.sql).
5. Make sure the SQL server setup is complete and it is up and running with the "clgmgmt" database.

Short Introduction :

This is a simple console based python application which uses an external Database server to store and retrieve the data required for its operations.

The operations include :
. Creation/Deletion/Edition of a student from the database
. Student and Parent information search.
. Attendance Manipulation operation for all the months

----------------------------------------------

For details editing operation, enter the field name as the attribute name from the database tables.
For attendance related operations, enter the months in this format (jan/feb/mar/apr/may/jun/jul/aug/sept/oct/nov/december)

----------------------------------------------

Note for the Developers : 

Attendance.py contains all the attendance management operations.

ConFrontend.py contains the info display operations for student/parents.

DbManip.py contains all the data manipulation operations into the database, including traversing.

StudClass.py contains the container classes for the information of students and parents.

main.py is the main entry point where the program execution begins.

----------------------------------------------

IMPORTANT NOTE :

On line 9 of main.py, change the unix_socket="" to the path of your sql installation where the server is installed (For Linux/Unix users).

Windows user should completely omit that argument altogether by deleting it from the code before running. 

Windows : con = MySQLdb.connect("localhost","root","","clgmgmt")
Linux/Unix : con = MySQLdb.connect("localhost","root","","clgmgmt",unix_socket='/opt/lampp/var/mysql/mysql.sock') (This is for default XAMPP installation, change it to your socket path)

You can also change the server path ("localhost"), username to sql server ("root") and password ("") according to your connection needs.

----------------------------------------------

STEPS TO RUN:

execute main.py using the terminal of your choice.

"python main.py"

----------------------------------------------

Feel free to try out my project, make your own implementations, suggest changes and modification and help in improving my project. :)

----------------------------------------------

P.S. : Hail the internet for all the awesome resources and information present on anything you want to learn. Credits to everybody who made it possible for me to complete this project of mine. :)