
#This Program was developed by M.Anish to show flaws of eval() in python3.
#Giving __import__('os').system("<malicious command> ") can damage such a system.
import getpass

passwd=1234
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
