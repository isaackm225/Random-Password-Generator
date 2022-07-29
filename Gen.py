import random
import secrets
import string
from UI import ui

def Gen(param: tuple)->string:
  """Returns a complicated string based on the param"""
  
  chars={
  "low": "",
  "up": "",
  "digits":None,
  "symbol":None
  }
  pwd=""

  s,d,l=param
  if s is True:
    chars["symbole"]=""
  if d is True:
    chars["digits"]=""
  for i in range(l):
    chars["low"].join(secret.choice(string.ascii_lowercase))
    chars["up"].join(secret.choice(string.ascii_uppercase))
    try:  
      chars["digits"].join(secret.choice(string.digits))
      chars["symbol"].join(secret.choice(string.punctuation))
    except:
      pass

  for string in chars.values():
    if string != None:
      passwd+=string

  return passwd[:l]


  while True:
    if passwd[:l].contains(""):
      return passwd 
    else:
      random.shuffle(passwd)




Gen(ui())


  

"""unpack param
initialize the pool tuple
add param if they =True
initialize dict
set default(var->const)

for i in range(round(l/len(pool_tuple))):
	for item in pool:
		item.join(secrets.choice(dict[item]))"""


