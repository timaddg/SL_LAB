stud={1:'asha',2:'dutt',3:'rekha',4:'amogh'}
list1=["value2","value2","value3","value4"]
list2=[""]
i=0
j=0
k=0
for i in stud:
print('key is',i,'value is',stud[i])
list1[j]=stud[i]
list2[k]=i
j=j+1

print( 5 in list1)
print(list2)
print(stud.keys())
print(stud.values())
print(stud.items()