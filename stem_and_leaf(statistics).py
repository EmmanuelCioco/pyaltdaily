values=[3, 8, 12, 19, 24, 27, 31, 35, 42, 46, 53, 57, 61, 75, 89]
values=values.sort()
arrangement_of_values()
stem=[]
leaf=[]
stemleaf_dict{}
for i in values:
  i=str(i)
  length=len(i)
  if length==1:
    stem=stem.append(0)
    leaf=leaf.append(i)
