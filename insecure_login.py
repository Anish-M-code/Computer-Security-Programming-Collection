
#This Program was developed by M.Anish to show flaws of eval() in python3.

import getpass

passwd='a'
user=input('Enter username:')
password=getpass.getpass('\nEnter PIN:')
password=eval(password)
try:
 if passwd==password:
   print('Successfull Login!')
 else:
   print('Login Failed! :( ')
except NameError:
   print('PIN should be a valid integer!')
   print('Exiting...') 
