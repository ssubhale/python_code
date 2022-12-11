##  Methods in string

A = '''Python Language'''
B = ''' Java Language '''

#1. strip() - It removes whitespaces from string
print('strip =>',B.strip())
#  lstrip() - It removes whitespaces from leftside of strring
print('lstrip =>',B.lstrip())
#  rstrip() - It removes whitespaces from rightside of string
print('rstrip =>',B.rstrip())


#2. lower() - It convert string into lowercase
print('lower =>',A.lower())


#3. upper() - It convert string into uppercase
print('upper =>',A.upper())


#4. replace() - It replaces the old character or set of new characters by new
print(A.replace('a','#'))
print(B.replace('v','V'))


#5. capitalize() - It converts first char of string into uppercase and remaining into lowercase
print(A.capitalize())
print(B.capitalize())


#6. split() - It splits the string into list of substrings separated by separator.
            # By default separator is space. 
print(A.split())
print(B.split())
print(A.split('a'))
print(B.split('a'))


#7.count() - It returns count of string
#  count(value,start,end)  start(0) and end(-1) are optional
print(A.count('a'))
print(B.count('a'))
print(A.count(' '))
print(B.count(' '))
print(A.count('a',6,15))
print(B.count('a',6,15))


#8. find() - It returns index of first occurence of charactor. Returns -1 when not found. find(value,start,end)
print(A.find('a'))
print(B.find('a'))
print(A.find('z'))
print(B.find('n'))


#9. index() - It is same as find. it generate Error when not found
print(A.index('a'))
print(B.index('a'))
#print(A.index('z'))#ValueError: substring not found
print(B.index('n'))


#10. isalpha() - It returns True when whole strig contains only alphabates
print(A.isalpha())
print(B.isalpha())


#11. isdigit() - It returns True when whole strig contains only digits
print(A.isdigit())
print(B.isdigit())


#12. islower() - It returns True when whole strig contains only lowercase alphabates
print(A.islower())
print(B.islower())


#13. isupper() - It returns True when whole strig contains only uppercase alphabates
print(A.isupper())
print(B.isupper())


#14. title() - converts first charactor of each word into uppercase
C = """shrikrishna ubhale"""
print(C.title())


#15. swapcase() - convert lower into uppercase and upper into lowecase
D = """sHRIKRISHNA uBHALE"""
print(D.swapcase())


#16. isspace() - returns True when string is containing only empty space 
X = '''   '''
print(X.isspace())
