
pass_new = ''

def asi(m,n):
    for i in m:
      global pass_new
      asin = ord(i)-65
      pass_new = pass_new + n[asin]
      
def generate(x,y,z,x_choice,y_choice,z_choice):
     global pass_new
     pass_new = ''    
     asi(x,x_choice)
     y2 =int(y)
     pass_new= pass_new + y_choice[y2]
     asi(z,z_choice)
     return (pass_new)

  
  
