
''' 
 Unblock Origin 2.0
 Copyright (C) 2018-2020 M.Anish <aneesh25861@gmail.com>

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.
 '''
 
 # A crossplatform website unblocker in python !
try:

     import platform
     import webbrowser
     import os
     
except ImportError:

      print('\nCritical Error: Necessary modules were not found!')
      ch=input()
      exit(1)

url=''

def system(x):
   return os.system(x)

def cls():
  if platform.system().lower()=='windows':
     x=os.system('cls')
  else:
     x=os.system('clear')
     
def check_internet():
   if (os.system("ping tails.boum.org")!=0):
        cls()
        print(" \nInternet Connection is Not Available!\n ")
        ch=input()
        exit(1)
   cls()
       
def get_url():
  print('\n Enter url: ',end='') 
  global url
  url=input()
  
def web_request(service):
   webbrowser.open(service+url)
   
def web_request2(service1,service2):
   webbrowser.open(service1+url+service2)
   
def web(service):
   webbrowser.open(service)
   
def google_cache():
    web_request("https://webcache.googleusercontent.com/search?q=cache:")
    
def google_weblight():
    web_request("https://googleweblight.com/i?u=")

def internet_archive():
    web_request("https://web.archive.org/save/_embed/")
    
def archive_fo():
    web_request("https://archive.fo/?run=1&url=")


def searx():
    web_request2("https://searx.info/?q=","&categories=general&language=en-US")

def startpage():
    web_request("https://www.startpage.com/do/search?&q=")

def proxysite():
    web_request2("https://eu6.proxysite.com/process.php?d=","&b=1")

def cloud():
    web_request("https://via.hypothes.is/")

def kproxy():
    web("https://kproxy.com/")

def hidester():
    web("https://hidester.com/proxy/")

def hideproxy():
    web("https://hide.me/en/proxy")

def hma():
    web("https://www.hidemyass.com/proxy")

def pdfcrowd():
 web("https://pdfcrowd.com/")

def pdfmyurl():
 web("https://pdfmyurl.com/")

def load(x):
    if x==1: 
       archive_fo()
       menu()
    elif x== 2: 
       internet_archive()
       menu()
    elif x==3: 
       google_cache()
       menu()
    elif x==4: 
       google_weblight()
       menu()
    elif x==6: 
       startpage()
       menu()
    elif x==5: 
       searx()
       menu()
    elif x==7: 
       cloud()
       menu()
    elif x==8: 
       pdfcrowd()
       menu()
    elif x==9: 
       pdfmyurl()
       menu()
    elif x==10: 
       proxysite()
       menu()
    elif x==11: 
       hidester()
       menu()
    elif x==12: 
       kproxy()
       menu()
    elif x==13: 
       hideproxy()
       menu()
    elif x==14:  
       hma()
       menu()
    else: 
       menu()
       exit(0)
    

def menu():
  i=0
  ch=''
  cls()
  print("\n Select services given below to unblock website. \n")
  print("Difficult To Block Services\n\n 1)Archive Fo \n 2)Internet Archive \n 3)Google Cache \n 4)Googleweblight \n 5)Searx \n 6)Startpage \n 7)Hypothes.is \n 8)Webpage to pdf using pdfcrowd \n 9)Webpage to pdf using pdfmyurl \n\nProxy Sites \n\n 10)Proxysite \n 11)Hidester Proxy \n 12)Kproxy  \n 13)Hide.me Proxy\n 14)HMA Proxy \n\nEnter Choice:")
  while(1):
     try:
      i=int(input())
      break
     except ValueError:
      print("\n Please Enter a valid integer as a choice!:")
  load(i)

def main():
   check_internet()
   get_url()
   menu()
   ch=input()   

main()
