#Exercice1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30] 

dict_from_list = dict(zip(keys,values))
print(dict_from_list)

#Exercice2
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

new_dict = dict1.copy()
new_dict.update(dict2)
print(new_dict)

#Exercice3
sampleDict = {
       "class": {
              "student": {
                     "name": "Mike",
                     "marks": {
                            "physics": 70,
                            "history": 80
                            }
               }
       }                   
} 

print(sampleDict["class"]["student"]["marks"]["history"])

#Exercice4

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

new_dict = dict.fromkeys(employees,defaults)
print(new_dict)

#Exercice5
sample_dict = {}
sample_dict = {
       "name": "Kelly",
       "age": 25,
       "salary": 8000,
       "city": "New york"}
# Clés à extraire
keys = ["name", "salary"]
new_dict = {}
for key,value in sample_dict.items():
       if(key in keys):
              new_dict[key] = value

print(new_dict)

#Exercice6
keys = ["name", "salary"]
new_dict = {}
for i in keys:
       sample_dict.pop(i)

print(sample_dict)

#Exercice7
sample_dict = {'a': 100, 'b': 200, 'c': 300}

for kay,value in sample_dict.items():
       if(value == 200):
              print('200 present in a dict')

#Exercice8
sample_dict = {
 "name": "Kelly",
 "age":25,
 "salary": 8000, 
 "city": "New york"
}

sample_dict["location"] = sample_dict["city"]
del sample_dict["city"]
print(sample_dict)

#Exercice9
sample_dict = {
 'Physics': 82,
 'Math': 65,
 'history': 75
} 

minimum = min(sample_dict, key=sample_dict.get)  # Just use 'min' instead of 'max' for minimum.
print(minimum, sample_dict[minimum])

#Exercice10
sample_dict = {
 'emp1': {'name': 'Jhon', 'salary': 7500},
 'emp2': {'name': 'Emma', 'salary': 8000},
 'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict['emp3']['salary'] = 8500
print(sample_dict)
