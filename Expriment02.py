#tower of hanoi problem
def hanoi(n,source,auxillary,target):
    if(n>0):
        hanoi(n-1,source,target,auxillary)
        print(f"Move disk{n} from {source} to {target}")
        hanoi(n-1,auxillary,source,target)
num_disk=int(input("Enter the number of disk:"))
hanoi(num_disk,'A','B','C')

#Lambda function to find a greater of 2 input numbers
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
greater=lambda x,y:x if x>y else y
result=greater(a,b)
print(f"The greater number between {a} and {b} is {result}")

#Using map function perfom element wise additon of elements of two lists.
input_list01=input("Enter space seperated numbers in list 1:")
list01=list(map(int,input_list01.split()))
input_list02=input("Enter space seperated numbers in list 2:")
list02=list(map(int,input_list02.split()))
sum_=map(lambda a,b:a+b,list01,list02)
sum_list=list(sum_)
print(sum_list)

#Using map and filter find the cube of all the odd numbers from the given input list.
input_list=input("Enter space seperated numbers in list:")
list_=list(map(int,input_list.split()))

count_cube_odd_numbers=list(map(lambda x:x**3,filter(lambda x:x%2!=0,list_)))

print("Original list:",list_)
print("List of cubed odd numbers in the original list:",count_cube_odd_numbers)


