#python is an oops concept:

#Session 1 ->compelete programming
#session 2 ->Probem solving:tc sc
#session 3:-> approacing to realtime projects: parsing of json DATA or Database data


#print statements in python
print("hellolslkdk")
name = "ameen"
age = 25
print("the name is ",name," the age is ",age)
print(f"the name is {name} and the age is {age}")
print("the name is {} and the age is {}".format(name,age))


a = 10
print(type(a))


#statements in python
#1. conditional statements: if, elif, else
#2. iterative statements: for, while
#3. unconditional statem: break, continue, 


#greates of 3 numbers
# a,b,c = input("enter the sting").split(",")
# print(a)
# print(b)
# print(c)

a = 10
b= 300
c  = 3
#relational operation: >,<,<=,>=, ==,!=
#logical operation: and or union,intersection, defference
if (a>b or a>c):
    print(a," is greater")
elif(b>a or b>c):
    print(b," is greater")
else:
    print(c," is greater")
n =9
# n = int(input("enter the number to check even or odd"))
if n%2==0:
    print("even")
else:
    print("odd")
#iterative statement
#syntax of range(start,end,step)

for i in range(8):
    print(i)
for i in range(1,11):
    print(i)
for i in range(1,11,2):
    print(i)
for i in range(1,11):
    if i%2 == 0:
        print(i)

#print 1-10 using while
i = 1
while(i<=10):
    print(i)
    i =i +1
#unconditional statement
#continue(skip)
#break(terminate)
#1-10 except 5
for i in range(1,11):
    if i == 5:
        continue
    print(i)
#to find n natural number using for loop
#n=10
summ = 0
for i in range(1,11):
    summ = summ + i
print("the sum is : ",summ)

#1-10, 10-1
#printing number from 10 to 1
for i in range(10,0,-1):
    print(i)

#fibonacci program
#5-> 0 1 1 2 3
#program 
n = 5#user input


f1 = 0
f2 = 1
if n == 1:
    print(f1)
elif n == 2:
    print(f1," ",f2)
else:
    print(f1," ",f2)
    for i in range(3,n+1):
        # 0 1 1 2 3
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        print(f3," ")
#operators:>> <<
#very important
#data structures:
#1.Built in datastructeres: list,tuple,set, dictionary
#2.User defined datastructeses: stack,queue,linkedlist, tree, graph

#1.Built in data structures
#list: list is an sequence of mixed datatype enclosed within a square brackets
l = [10,10.2,"alen",[10,20,30]]
print(type(l))
l = [10,20,30,40]
print(l)

#Accessing element using index
print(l[0])
print(l[3])
print(l[-1])#iloc[rows,column]

#slicing in list
print(l[0:3])
print(l[1:3])
l = [10,20,30,40]
print(l[::-1])

#length ->len(list)
l = [10,20,30,40]
print(len(l))

#count
l = [1,22,3,44,5,22,22]
print(l.count(22))

#reversed(list)
l = [4,3,2,1]
res = list(reversed(l))
print(res)
#sum,min,max
l = [1,2,3,4,5,111,6,7,8,9,10]
print(sum(l))
print(min(l))
print(max(l))
#operations in list
#list is MUTABLE(can be changed)
l = [10,20,30]
#addig the elemets in list
#1. list.append(ele)
l.append(40)
print(l)
#2. list.insert(pos,ele)
l.insert(1,15)
print(l)
#3. list.extend(ele)
#10,15,20,30,40
l.extend([50,60,70])
print(l)
#10,15,20,30,40,50,
#delete the element in list
#pop(), remove(),clear, del

l.pop()
print(l)
l.pop()
print(l)

#list.remove(ele)
l.remove(15)
print(l)
#l.clear()
# l.clear()
# print(l)

#del l
# del l
# print(l)


#sorting in list
#l.sort()
#sorted(list)
l =[1,22,4,6,3,5]

# print(l.sort())
print(sorted(l))


#list() methods
t = (10,20,30,40,500)
print(type(t))
l = list(t)
print(type(l))


# n = eval(input("enter the number"))
# print(n)


#Tuple: elements enclosed in ()
#Tuple are IMMUTABLE(can't be changeD!!)

t = (10,20,30,40,50)

print(type(t))
print(t)
#length
t = (10,20,30,40,50)
print(len(t))
#sum, min,max
print(sum(t))
print(min(t))
print(max(t))


#accessing element of tuple
t = (10,20,30,40,50)
print(t[2])
print(t[-1])

#slicing in tuple
print(t[1:])
print(t[::-1])

#tuple() method
s = {10,20,30,40}
t = tuple(s)
print(t)
print(type(t))

t = (10,)
print(type(t))

#set 
s = {}#emplty set
print(type(s))
#empty set
s = set()
print(s)
print(type(s))

#Note: set only prints unique value
s = {11,22,22,33,44,32,22,33}
print(s)


#set() methods
l = [10,20,30]
s = set(l)
print(s)

#operations in set
#union, intersection, difference
s1 = {10,20,30,40}
s2 = {30,40,50,60}

print(s1.union(s2))
print(s1 | s2)
print(s1.intersection(s2))
print(s1 & s2)
print(s1.difference(s2))
print(s1 - s2)

#dictionary  in pytho
d = {}
print(type(d))
d = dict()
print(type(d))

d = {1:10,2:20,3:30,4:40}
print(d[3])

d = {'Name':'Alen','Age':20}
print(d['Name'])
print(d['Age'])

#length
print(len(d))
#insert elments in dict
d['class'] = 'CSE'
print(d)
#nOTE : Dict are MUTABLE
#update
d['Name'] = 'Bob'
print(d)
d1 = {1:10,2:20}
d2 = {3:30,4:40}
d1.update(d2)
print(d1)


#deleting elments in dict
#del, clear()

d = {'Name':'Alen','Age':20}
# del d 
# print(d)
# d.clear()
# print(d)


#methods: items(),keys(),values()

d = {'Name':'Alen','Age':20}
print(d.items())

#keys()
print(d.keys())
print(d.values())

#iteration in dictiory
d = {'Name':'Alen','Age':20}
#print(d['Name'])=>d[Key]
for i in d:
    #print(i)
    # print(d[i])
    print("key:",i," values: ",d[i])


#in and not in->list,tuple,set
fruits = ["apple","mango","banana"]
for elements in fruits:
    print(elements)

if 'apskjple' not in fruits:
    print("True")
else:
    print("false")


#Functionns
def add():
    a = 10
    b = 20
    print(a+b)
add()

def add(x,y):
    a = x
    b = y
    print(a+b)
add(20,40)

#return
def add(x=30,y=100):
    a = x
    b = y
    return a+b
res = add()
print(res)
#CCNA: Routers and switches



#OOPs in pythons
'''
1.Class and objects
2.Constructor
3.Inheritence
4.Encapsulation
5.Abstraction
6.Polymorphism
'''
#1.Class and Objects
class Student:
    #instence variable
    rollno = "IS01"
    name = "alen"
    def student_details(self):
        #local variables
        myname = "ameen"
        print("functionn name is: ",myname)
obj = Student()

print(obj.rollno)
obj.student_details()



class Student:
    #instence variable
    a = 400
    def student_details(self):
        #local variables
        a = 50
        print(self.a)#to access instence variable in functions
obj = Student()
obj.student_details()


#2.Constructor
class Student:
    #costructor
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    def student_details(self):
        print("The name is ",self.name," the age is: ",self.age)

obj = Student("alen",50)
obj.student_details()

#3.Inheritence
#parent class->base class,super class
#child class->derived class,sub class

#single level inheritence

class Parent:
    def pdisplay(self):
        print("Parent display")

class Child(Parent):
    def cdisplay(self):
        print("child display")

c = Child()
c.pdisplay()

#multiple inheritence
class Father:
    def fdisplay(self):
        print("Father display")
class Mother:
    def mdisplay(self):
        print("Mother display")

class Child(Father,Mother):
    def cdisplay(self):
        print("child property")
c = Child()
c.mdisplay()
c.fdisplay()



#encapsulation
#__(underscore underscore)
class Encap:
    a = 10
    def displaly(self):
        print("this is function property")

c = Encap()
print(c.a)

#protected
class Encap:
    __a = 100#protected
    def displaly(self):
        print(self.__a)

c = Encap()
c.displaly()
#abastraction
from abc import ABC,abstractmethod
class AbstractClass(ABC):
    @abstractmethod
    def myabsmethod(self):
        None
class ConcreteClass(AbstractClass):
    def myabsmethod(self):
        print("this is abstract method!!")
obj = ConcreteClass()
obj.myabsmethod()

#polymorphism
#1.overloading:1.operator ol(+,*),2.method ol

'''

l  = [10,20,300]
print(l*3)

add()
add(x,y)
add(x,y,z)
'''
#2.overriding
class Parent:
    def display(self):
        print("hello")
class Child(Parent):
    def display(self):
        print("child hello")
c = Child()
c.display()


#lambda,map,reduce,filter
g = lambda x:x*2
print(g(2))


#fileter
#syntex: filter(lambda,list)
l = [1,2,3,4,5,6]
final_list = list(filter(lambda x:x%2==0,l))
print(final_list)


#map(lambda,list)
#l = [10,20,30] = [110,120,130]
l = [10,20,30]
final_list = list(map(lambda x:x+100,l))
print(final_list)


#reduce funnction reduce(lambda,list)
import functools
l = [1,2,3,4,5,6,7,8,9,10]
final_list = functools.reduce(lambda a,b:a+b, l)
print(final_list)



#math function in pytho

import math
n = 25
# print(dir(math))
print(math.sqrt(n))
n =5#150
print(math.factorial(n))


#USER DEFINED DATASTRUCES
#1.LINEAR DS:STACK,QUEUE,LINKEDLIST,ARRAY
#2.Non linear DS: Graphs,trees


#Stacks
#LIFO
'''
Implementation of stacks can be done in two way
1. List
2.Modules
'''
#1.List
'''
push->insertinng the element in stack
pop -> removign the lement in stack

'''
# ->[10,30,40,50]
'''
IN LIST
push->usig append method of list
pop-> usig pop method of list
'''
#method 1: list
stack = []
#addind or pushing element
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
print(stack)

#pop
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
# stack.pop()
# print(stack)


#to check stack is empty or not
if len(stack) == 0:
    print("The stack is empty")

if not stack:
    print("stack is emplty")



#COMPLETE PROGRAM TO DEMONSTRATE THE STACK usig LIST

stack  = []
def push():
    ele = input("Enter the elment of stack")
    stack.append(ele)
    print(stack)

def pop_ele():
    #stack is empty 
    if not stack:
        print("Stack is empty!!!")
    else:
        e = stack.pop()
        print("The removed element is: ",e)
        print(stack)
# while True:
#     print("Select the options: 1.push 2.pop 3.quit")
#     choice = int(input("Enter your choice"))
#     if choice == 1:
#         push()
#     elif choice == 2:
#         pop_ele()
#     elif choice == 3:
#         break
#     else:
#         print("Enter correct options")

#method 2: modules
'''
collections->deque()
push ->append()
pop->pop()
'''
import collections
stack = collections.deque()
print(stack)

stack.append(10)
stack.append(20)
stack.append(30)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
#is emplty or not
if not stack:
    print("stack is emplty")
else:
    print("stack is full")


#QUEUE
#FIFO
'''
1.enqueue->adding elements(rear/tail)
2.dequeue->deletimg elements(front)
[10]

IMPLEMENTATIO OF QUEUE CAN BE DONE IN 2 WAYS
1. list
2.modules
'''
#list
#add->append
#dele->pop(0)
# [10,20,30,40]
#pop(0)-----------append(ele)
queue = []
queue.append(10)#[10]
queue.append(20)#[10,20]
queue.append(30)#[10,20,30]
print(queue)
#deleting e(dequeue)
queue.pop(0)
print(queue)
queue.pop(0)
print(queue)
queue.pop(0)
print(queue)
if not queue:
    print("Queue is emplty")

#2 method in list[fifo]
#insert(0,ele)----------pop()
queue  =  []
queue.insert(0,10)#[10]
queue.insert(0,20)#[20,10]
queue.insert(0,30)#[30,20,10]
print(queue)
queue.pop()
queue.pop()
print(queue)
if not queue:
    print("Queue is empty!!")

#Complete program 
queue  = []
def enqueue():
    ele  = input("enter the element")
    queue.append(ele)
    print(queue)
def dequeue():
    if not queue:
        print("queue is emplty")
    else:
        queue.pop(0)
        print(queue)
# while True:
#     print("select option 1.enqueue 2.dequeue 3.quit")
#     choice  = int(input("Enter the option"))
#     if choice == 1:
#         enqueue()
#     elif choice == 2:
#         dequeue()
#     elif choice  == 3:
#         break
#     else:
#         print("Enter the correct option")

#linked 
'''
types of linked list
1.sinngle ll
2.doulble ll
3.circular ll

#single ll
Operations in linked list
1.addition: add at begin, add at middle,add at end
2.delete: delete at begin, delete at middle,delte at emd
3.traversinng of sll
'''
#node: data,ref of next node
class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
node1 =  Node(10)
print(node1.data)
#insert the add at begin 
class LinkedList:
    def __init__(self):
        self.head = None#emplty linked list
    def print_ll(self):
        if self.head is None:
            print("Linked list is emplty")
        else:
            n = self.head
            while n is not None:
                print(n.data, end=" ")
                n = n.ref
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head= new_node

ll = LinkedList()
ll.add_begin(10)
ll.add_begin(20)
ll.add_begin(30)
ll.print_ll()
