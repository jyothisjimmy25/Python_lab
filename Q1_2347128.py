#list
list=[10, 10, 15, 20, 25, 30, 35, 40, 45, 50]
#sub question is the list divisible by 3
d=[ x for x in list if x % 3==0]
print("num divisible by 3",d)

#square of even numbers in a list
a = [x ** 2 for x in list if x % 2 == 0]
print("squared even numbers:",a)

#sum of even digits in a list
b= [x + x for x in list if x % 2 ==0]
print("sum of even digits in the list:",b)

#remove duplicate numbers in the list
newlist=[]
for i in list:
    if i in newlist:
        continue
    else:
        newlist.append(i)
print(newlist)

#dictionary
employee = {
    'virat kohli': '5 November 1988',
    'mesh yadav': '25 October 1987',
    'manish pandey': '10 September 1989',
    'rohit sharma': '30 April 1987',
    'ravindra jadeja': '6 December 1988',
    'hardik pandya': '11 October 1993'
}

def birthDate(full_name):
    if full_name in employee:
        return employee[full_name]
    else:
        return "Employee not found"
    
a=input("enter the full name")
print(birthDate(a))
