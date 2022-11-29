def enc_fixer(asc,shift):
  while asc+shift > 122:
    n  = enc_fixer()
  
  

def encode(msg,shift):
  ls = list(msg)
  enc_txt = []
  for item in ls:
    asc = ord(item)
    if asc in range(97,123):
      mod_shift = (asc + shift - 97)%26 +97
      enc_txt.append(chr(mod_shift))
    else:
      enc_txt.append(item)
  print('Encrypted text -> ',''.join(enc_txt))
    

def decode(msg,shift):
  ls = list(msg)
  enc_txt = []
  for item in ls:
    asc = ord(item)
    if asc in range(97,123):
      mod_shift = (asc - shift - 97)%26 +97
      enc_txt.append(chr(mod_shift))
    else:
      enc_txt.append(item)
  print('Encrypted text -> ',''.join(enc_txt))