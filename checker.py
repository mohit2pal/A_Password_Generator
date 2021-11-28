import requests
import hashlib

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