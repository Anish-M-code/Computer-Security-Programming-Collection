# BRUTAL KAT
# Copyright (C) 2019-2020 M.Anish <aneesh25861@gmail.com>
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

import os
import platform

#Function to clear screen
def cls():
  x=os.system('cls' if platform.system().lower()=='windows' else 'clear')
  
cls()
print('''

                   .__....._             _.....__,
                     .": o :':         ;': o :".
                     `. `-' .'.       .'. `-' .'   
                       `---'             `---'  
             _...----...      ...   ...      ...----..._
          .-'__..-''----    `.  `"`  .'    ----''-..__`-.
         '.-'   _.--''        `-._.-'       ''---._   `-.`
         '  .-"'                  :                  `"-.  `
           '   `.              _.'"'._              .'   `
                 `.       ,.-'"       "'-.,       .'
                   `.                           .'
                     `-._                   _.-'
                         `"'--...___...--'"`

                   BRUTAL KAT: A Simple Keyword Search tool
            
               Developed by: M.Anish <aneesh25861@gmail.com>

''')

#Fastest scan mode exact match returns single occurence.
def scan(z,file):
 try:
          with open(file) as f:
           for x in f:
                 if z in x:
                     print('Search Hit!',x)
                     break
                 print(x)
 except:
    print('File Not Found!')
 
#scan mode exact match returns multiple occurences.
def scanm(z,file):
 try:
          with open(file) as f:
           for x in f:
                 if z in x:
                     print('\nSearch Hit!',x)
 except:
    print('File Not Found!')
 
#scan mode no case match returns single occurence.
def nscan(z,file):
 try:
          with open(file) as f:
           for x in f:
                 if z.lower() in x.lower():
                     print('Search Hit!',x)
                     break
                 print(x)
 except:
    print('File Not Found!')

#scan mode no case match returns multiple occurence.
def nscanm(z,file):
 try:
          with open(file) as f:
           for x in f:
                 if z.lower() in x.lower():
                     print('\nSearch Hit!',x)
 except:
    print('File Not Found!')

def menu():
  k=input('\n\nEnter Keyword:')
  fil=input('\nEnter Filename:')
  cls()
  print('\n\nMenu:-\n\n')
  print('''1)Search Exact Keyword and return line on First Occurance. \n2)Search Exact Keyword and return lines of all Occurances. 
3)Search Keyword (case insensitive) and return line on First Occurance\n4)Search Keyword (case insensitive) and return lines of all Occurance\n''')
  while 1:
    try:
        x=int(input('\nEnter choice:'))
        if x>0 and x<5:
         break
    except ValueError:
      print('Enter correct choice!')
  if x==1:
    cls()
    scan(k,fil)
  elif x==2:
    cls()
    print('\nScanning...\n')
    scanm(k,fil)
  elif x==3:
    cls()
    nscan(k,fil)
  else:
    cls()
    print('\nScanning...\n')
    nscanm(k,fil)  
menu()
wait=input('\nPress any key to exit...')