# -*- coding: utf-8 -*-
"""Geoduhub 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ia28FV5V0pX12JZqGQy2tGFN4zHKj3-H

# Data Types
"""

" integre, sequence,mapping,boolean,set,text"

"""# Sequence data types string"""

s="Welcome to Geoduhub"
print(s)

s[3:7]  #string slicing[Start:end:step]

s[8:10]

s[14:]

s[1:8:2]

s[1:8]

s[::-1]

s[-1:-4:-1]

s="hello"

del s

s='Hello'
s1=s
s1

"""# String Function"""

s="Hello Geoduhub"

len(s)

s.upper()

s.lower()

s="Hello"
s1="Hello Goeduhub"
s2=s+" "+s1

s2

s2*2

print('h' in s)

print('H' in s)

s2.lstrip()

s2.rstrip()

#largest of three number
a=int(input('Enter the value of A:'))
b=int(input("Enter the value of B: "))
c=int(input("Enter the Value of C: "))

if a>b and a>c:
  print('A is largest number')
  print(a)
if b>a and b>c:
  print('B is greater number')
  print(b)
if c>a and c>b:
  print("C is largest number")
  print(c)

age=int(input("enter number: "))
if age>=18:
  print('Person is Eligible for vaccination')
else:
  print("Person is not Eligible")

a=int(input("value of A is: "))
b=int(input("value of B is : "))

if b>a:
  print("b is greater")

elif a==b:
  print("a is equal to b")

else:
  print("b is not grater")

"""# Loops"""

#reusability
# don't write code again and again

# for loop

s="Hello"
for i in s:
  print(i)

a=[]
l=''
s="hello"
for i in s:
  a.append(i)
print(a)
print(l.join(s))

"""# Range Function"""

for i in range(10):
  print(i)

n=2
for i in range(1,11):
  t=n*i
  print(t)

"""# Star Pattern"""

r=int(input("Enter rows: "))
for i in range(0,r):
  for j in range(i):
    print("*",end=" ")
  print()

for i in range(6,0,-1):
  print(i)

for i in range(6,0,-4):
  print(i)

for i in range(5):
  print(i)
  if(i==3):
    break

for i in range(5):
  if(i==3):
    continue
  print(i)

numbers=[1,2,34,5,67,7,8,9,9,0,0,5,8,76,6,5,4,32,2,5,2,6]

for number in numbers:
  if number%2==0:
    pass
  else:
    print(number)

"""# While"""

i=0
s='Goeduhub'
while i<len(s):
  print(i)
  i+=1

i=0
s="goeduhub"
while i<len(s):
  if s=='d':
    break
  print(i)
  i+=1

r=[]
l=[1,2,34,5]
for i in l:
  print(i)

l.append(i)
print(l)

l.reverse()

l

l[3]=56
l

