#q1
def TowerOfHanoi(disks,source,destination,path):
    if disks==1:
        print("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(int(disks)-1,source,path,destination)
    print("Move disk",disks,"from source",source,"to destination",destination)
    TowerOfHanoi(int(disks)-1,path,destination,source)

#given 3 disks
disks=3
#Let A,B and C are the three rods
TowerOfHanoi(disks,'A','B','C')

#q2 iterative
""" iterative function to calculate Pascals Triangle """
rows=int(input("Enter number of rows:"))
for i in range(rows):
    print(''*(rows-i),end='')
    print(''.join(map(str,str(11**i))))

#q2 recursive
def pascals_triangle(rows):
    """ Recursive function to calculate Pascals Triangle """
    if rows == 1:
        return [[1]]
    else:
        result = pascals_triangle(rows-1) # Recursive call
        # Calculate current row using info from previous row
        current_row = [1]
        previous_row = result[-1] # Take from end of result
        for i in range(len(previous_row)-1):
            current_row.append(previous_row[i] + previous_row[i+1])
        current_row += [1]
        result.append(current_row)
        return result

rows=int(input("Enter number of rows:"))
triangle = pascals_triangle(rows)
for row in triangle:
    print(row)


#q3a
first_integer_as_divident=int(input("Enter a integer as divident:"))
second_integer_as_divisor=int(input("Enter another integer as divisor:"))
quotient=first_integer_as_divident//second_integer_as_divisor
remainder=first_integer_as_divident%second_integer_as_divisor
print("Quotient of two numbers is",quotient,"and the remainder is",remainder)
print(callable(remainder))
print(callable(quotient))
print(callable(first_integer_as_divident))
print(callable(second_integer_as_divisor))

#q3b
if(quotient==0):
    print("quotient is zero")
else:
    print("quotient is non zero")
if(remainder==0):
    print("remainder is zero")
else:
    print("remainder is non zero")


#q3c
list=list()
list.append(remainder)
list.append(quotient)
list.append(4)
list.append(5)
list.append(6)
print("old list:",list)
new_list=[]
for i in list:
    if i>4:
        new_list.append(i)
print("new list:",new_list)

#q3d
set=set(new_list)
print("set:",set)

#q3e
new_set=frozenset(set)
print("immutable set is:",new_set)
new_set.add(0)

#q3f
max=max(set)
a=print("max value:",max)
print("hash value:",hash(a))



#q4
class student:
    def __init__(self):
        self.name=name
        self.roll=roll
        return self.name,self.roll
    def __del__(self):
        return
name="Garvit"
roll="93"
student1=student
print(student1.__init__(student1))
del(student1)
print(student1.__init__(student1))


#q5a
class employee():
    def show_data(self):
        return f"Name of employee is {self.name} and salary is {self.salary}"
    def __del__(self):
        return

emp1=employee()
emp2=employee()
emp3=employee()

emp1.name="Mehak"
emp1.salary="40000"

emp2.name="Ashok"
emp2.salary="50000"

emp3.name="Viren"
emp3.salary="60000"

print("Before changing value of salary:")
print(emp1.show_data())

emp1.salary="70000"

print("After changing value of salary:")
print(emp1.show_data())


#q5b
del(emp3)

print(emp3.show_data())

#q6
from itertools import permutations
import enchant
d = enchant.Dict("en_US")
op=set()
word=str(input("Enter a word:"))
letters=[x.lower() for x in word ]
for n in range(len(word),len(word)+1):
    for y in list(permutations(letters,n)):
        z=(''.join(y))
        if len(z)>2:
            if d.check(z):
                op.add(z)
print(op)