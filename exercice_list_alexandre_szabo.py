# Exercice 1

list1 = [100,200,300,400,500]
list1.reverse()
print(list1)

# Exercice 2
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
new_list = []
if len(list1) == len(list2):
    for i in range(0,len(list1)):
        new_list.append(list1[i]+list2[i])
else :
    minlen = 0
    minlist = 0
    if(len(list1) > len(list2)):
        minlen = len(list2)
        minlist = 1
    else :
        minlen = len(list1)
        minlist = 2
    for i in range(0,minlen):
        new_list.append(list1[i]+list2[i])
    if(minlist == 1):
        for i in range(minlen,len(list1)):
            new_list.append(list1[i])
    else :
        for i in range(minlen,len(list2)):
            new_list.append(list2[i])

print(new_list)



# Exercice 3
numbers = [1, 2, 3, 4, 5, 6, 7]
new_list = []
for el in numbers:
    if(isinstance(el,int)):
        new_list.append(el*el)
    else :
        val = int(el)
        new_list.append(val*val)
print(new_list)

# Exercice 4

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

new_list=[]
for i1 in list1:
    for i2 in list2:
        if(isinstance(i2,str) and isinstance(i1,str)):
            new_list.append(i1+i2)
        else :
            new_list.append(str(i1)+str(i2))
print(new_list)

# Exercice 5
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
aff1 = ""
aff2 = ""

if len(list1) == len(list2):
    for i in range(0,len(list1)):
        print(f"list1: {list1[i]} <=> list2: {list2[len(list2)-(i+1)]}")
else :
    minlen = 0
    minlist = 0
    if(len(list1) > len(list2)):
        minlen = len(list2)
        minlist = 1
    else :
        minlen = len(list1)
        minlist = 2
    if(minlist == 1):
        for i in range(0,minlen):
            print(f"list1: {list1[i]} <=> list2: {list2[len(list2)-(i+1)]}")
        for i in range(minlen,len(list1)):
            print(f"list1: {list1[i]} <=> list2: too short")
    else :
        for i in range(0,minlen):
            print(f"list1: {list1[i]} <=> list2: {list2[len(list2)-(i+1)]}")
        for i in range(minlen,len(list2)):
            print(f"list1: too short <=> list2: {list2[len(list2)-(i+1)]}")


# Exercice 6

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
cpt = 0
for i in range(0,len(list1)):
    if(list1[i] == ""):
        cpt+=1
for i in range(0,cpt):
    list1.remove("")
print(list1)

# Exercice 7
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

def addElementAfterElement(base_list,new_val,cible):
    for index in range(0, len(base_list)):
        if(isinstance(base_list[index],list)):
            addElementAfterElement(base_list[index],new_val,cible)
        else :
            if(base_list[index] == cible and isinstance(base_list,list)):
                base_list.insert(index+1,new_val)

print()
addElementAfterElement(list1,7000,6000)
print(list1)

# Exercice 8
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

def addSubListInList(myList,second_List):
    done = False
    for index in range(0,len(myList)):
        if(isinstance(myList[index],list)):
            done = addSubListInList(myList[index],second_List)
    
    if(isinstance(myList,list) and done == False):
        for sub in sub_list:
            myList.append(sub)
    
    return True
        
print()
addSubListInList(list1,sub_list)
print(list1)

# Exercice 9
list1 = [5, 10, 15, 20, 25, 50, 20]
val = 20
new_val=200

    
for i in range(0,len(list1)):
    if(list1[i] == val):
        list1[i] = new_val

print(list1)

# Exercice 10
list1 = [5, 20, 15, 20, 25, 50, 20]
del_val = 20
cpt = 0
for el in list1:
    if(el == del_val):
        cpt+=1
for i in range(0,cpt):
    list1.remove(del_val)
print(list1)