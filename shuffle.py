import random

def shuffl(tem):
  x_list= []
  for i in tem:
      x_list.append(i)
    
  # print(x_list)
  
  random.shuffle(x_list)
  
  # print(x_list)

  x_choicenew=''

  for i in x_list:
      x_choicenew= x_choicenew + i
  
  return(x_choicenew)
