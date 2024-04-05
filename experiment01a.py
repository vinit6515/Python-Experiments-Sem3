#list functions
my_list=[1,2,3,4,5]

length=len(my_list)
print(length)

my_list.append(6)
print(my_list)

my_list.extend([7,8,9])
print(my_list)

my_list.insert(0,0)
my_list.insert(2,3)
my_list.insert(9,8)
print(my_list)

my_list.remove(3)
print(my_list)

popped_element=(my_list.pop(9))
print("popped element:",popped_element)
print(my_list)

index=my_list.index(4)
print("Element at index 4 is:",index)

count=my_list.count(3)
print("3 appears in the list",count,"times.")

my_list01=[0,8,0,5,2,0,0,4]

my_list01.sort()
print(my_list01)

my_list01.reverse()
print(my_list01)

my_list01.clear()
my_list.clear()
print(my_list)
print(my_list01)

#funstions of the tuple
my_tuple=(1,2,3,4,5,6)
my_list=[1,2,3]

print(my_tuple)

first_element=my_tuple[0]
sliced_tuple=my_tuple[1:4]
print("first element is:",first_element)
print("Elements are:",sliced_tuple)

my_tuple01=(7,8,9)

cocatenated_tuple=my_tuple+my_tuple01
print(cocatenated_tuple)
repeated_tuple=my_tuple*2
print(repeated_tuple)

length=len(my_tuple)
print("Length of the tuple is:",length)

count_of_an_element=repeated_tuple.count(2)
print("2 appears in the repeated tuple",count_of_an_element,"times.")

index_of_element=my_tuple.index(4)
print("4 is present at",index_of_element,"position.")

is_present=3 in my_tuple
print(is_present)

for item in my_tuple01:
    print(item)

my_tuple02=tuple(my_list)
print(my_tuple02)

#funtions of sets
my_set={1,2,3,4,4,3,5}

print(my_set)

my_set.add(0)
print(my_set)
my_set.update([6,7])
print(my_set)

my_set.remove(0)
print(my_set)
my_set.discard(8)
popped_element=my_set.pop()
print("Element popped:",popped_element)

set1={1,2,3,7}
set2={3,2,1,4,5}

union_set=set1.union(set2)
print("Union of two sets:")
print(union_set)
intersection_set=set1.intersection(set2)
print("Intersection of two sets:")
print(intersection_set)
difference_set=set1.difference(set2)
print("Difference in two sets:")
print(difference_set)
symmetric_difference_set=set1.symmetric_difference(set2)
print("Symmetric difference of two sets:")
print(symmetric_difference_set)

copied_set=my_set.copy()
print(copied_set)

is_present=4 in copied_set
print("4 is present in the set:",is_present)

length=len(copied_set)
print("the length of the copied set is:",length)

my_set.clear()
print(my_set)
copied_set.clear()
print(copied_set)

#functiond of dictonaries
my_dict={'Name':'VINIT','Age':18,'City':'Mumbai'}

name=my_dict['Name']
age=my_dict.get('Age',0)
non_existing_key=my_dict.get('non_existing_key','Not found')
print(name)
print(age)

print(my_dict)

my_dict['Age']=19
my_dict['Country']='India'
my_dict.update({'City':'Maharashtra','ZipCode':400097})

print(my_dict)

del my_dict['ZipCode']
removed_country=my_dict.pop('Country')

print(my_dict)
print(removed_country)

keys=my_dict.keys()
values=my_dict.values()
items=my_dict.items()
print(keys)
print(values)
print(items)

if_name_exists='Name' in my_dict
print(if_name_exists)
if_Country_exists='Country' not in my_dict
print(if_Country_exists)

length=len(my_dict)
print('Length of the dictionary is:'+str(length))
copy_dict=my_dict.copy()


for key in my_dict:
    print(key)
for value in my_dict.values():
    print(value)
for key, value in my_dict.items():
    print(key, value)




