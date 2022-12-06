##import statements.

#_import statement is used to achive communication between difrent python modules/files.
#_generally all file must be there in same location.
#_in import statament function defination and variable declaration
#   are skiped, but print statement and function calling are executed
#_there are four way to import.

#1. Simple import statement
# Here we use module name and dot(.) to access the contents.if there are same variables in two files then allways used simple import statement

#syntax : import <modul_name>

no1 = 18
no2 = 5

import Import1


Import1.mul(no1,no2)
Import1.floordiv(no1,no2)
