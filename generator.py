
x=""
pass_new = ""

x_choice = "qwertyuioplkjhgfdazxvbnm,./;;'['']][[>:>?{}{}\[-0909876531@!@#$%^*()--==9&^&%$@!!QWE45TVTBUM<O>??|\(*^7t^&55RE$%56954655494654987*/*+26!###^&)"
y_choice = "QWERTYUIOPASDFGHJZXCVBNMqwertyuiopasdfghklzcbnm1213456789064fds64r645454e65454466584674656634846538543454345454356'.;;.]/';303-923928782736333+*/3-3-3+2362+329+3/2*3/2+38+2398"
z_choice = "12039120938210948214294872198472140172!*(#&!*&!&#^!&#!#!(#^!)#)!#!)#^!#6484654546465468548498*/***/**/*/*/*/*/-+++--*-/-/*-/_+_{}{|:>{)_(*&^%%#@"

def asi(m,n):
    for i in m:
      asi = ord(i)-65
      global pass_new
      pass_new = pass_new + n[asi]
      
def generate(x,y,z):
#   x=input('Enter your name')
#   y=int(input('Enter your age'))
#   z=input('Enter your passion')
#   adj=input('Enter a master password')
  global pass_new
  asi(x,x_choice)
  y2 =int(y)
  pass_new= pass_new + y_choice[y2]
  asi(z,z_choice)
  return (pass_new)

#   print(pass_new)
  
  
