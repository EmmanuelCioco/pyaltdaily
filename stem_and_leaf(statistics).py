values=[3, 8, 12, 19, 24, 27, 31, 35, 42, 46, 53, 57, 61, 75, 89]
def arrangement_of_values():
  c=0
  while True:
      try:
          m=values[c]
          n=values[c+1]
      except IndexError:
          break
      if m>n:
          K=m
          m=n
          values[c]=m
          n=K
          values[c+1]=n
      c+=1
def length_of_last_values():
  
