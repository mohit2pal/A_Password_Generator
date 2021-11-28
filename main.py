import random
import requests
import hashlib

x=""
pass_new = ""
x=input('Enter your name')
y=int(input('Enter your age'))
z=input('Enter your passion')
adj=input('Enter a master password')

x_choice = "qwertyuioplkjhgfdazxvbnm,./;;'['']][[>:>?{}{}\[-0909876531@!@#$%^*()--==9&^&%$@!!QWE45TVTBUM<O>??|\(*^7t^&55RE$%56954655494654987*/*+26!###^&)"
y_choice = "QWERTYUIOPASDFGHJZXCVBNMqwertyuiopasdfghklzcbnm1213456789064fds64r645454e65454466584674656634846538543454345454356'.;;.]/';303-923928782736333+*/3-3-3+2362+329+3/2*3/2+38+2398"
z_choice = "12039120938210948214294872198472140172!*(#&!*&!&#^!&#!#!(#^!)#)!#!)#^!#6484654546465468548498*/***/**/*/*/*/*/-+++--*-/-/*-/_+_{}{|:>{)_(*&^%%#@"
def asi(m,n):
   for i in m:
      asi = ord(i)-65
      global pass_new
      pass_new = pass_new + n[asi]

asi(x,x_choice)
pass_new= pass_new + y_choice[y]
asi(z,z_choice)

print(pass_new)


def fid(pastwd):
    
    sha_pass= hashlib.sha1(pastwd.encode()).hexdigest()
    sha5= sha_pass[0:5]
    sha_rest= sha_pass[5:].upper()
    
    url= 'https://api.pwnedpasswords.com/range/' +sha5
    
    payload={}
    headers={}
    
    response = requests.request("GET", url, headers=headers, data=payload)
    
    pwnd_dict = {}
    
    pwnd_list = response.text.split("\r\n")
    for pwnd_pass in pwnd_list:
        pwnd_hash = pwnd_pass.split(":")
        pwnd_dict[pwnd_hash[0]] = pwnd_hash[1]
        
    if sha_rest in pwnd_dict.keys():
        return('found')
    else:
        return('woohoo')
        


fid_result = fid(pass_new)
if(fid_result == 'found'):
    print('Namaste found')
elif(fid_result == 'woohoo'):
     print('Namaste')   
    
    
    
    
                                                                                                                                                                                                            
