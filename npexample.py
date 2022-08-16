import numpy as np
#1 (10,15,30,45,60) create a numpy array
#2 (5to15) create a numpy array
#3 (50to100) create array which increases 5 by 5
#4 create an array has 10 members which has only "0"
#5 create an array has 10 members which has only "1"
#6 create numbers between 0to100 has equal absolute
#7 create 10 to 30 5 random integer
#8 [-1 to 1] create 10 numbers
#9 create a 3x5 matrix
#10 find rows and cols total in a 3x5 matrix
#11 find the value of min and max valued members in array
#12 find the indexes of min and max valued members in array
#13 select the first 3 element in an array
#14 reverse an array
#15 select the first row in array
#16 print the member which is in second row and third column
#17 choose the members which is  first member for each row
#18 squaring for each member in array
'''
#1
'''
a = np.array([10,15,30,45,60])
print(a)

'''
#2
'''
b = np.arange(5,15)
print(b)
'''
#3
'''
c = np.arange(50,100,5)
print(c)

'''
#4
'''
d = np.zeros(10)
print(d)
'''
#5
'''
e = np.ones(10)
print(e)
'''
#6
'''
f = np.linspace(0,100,5)
print(f)
'''
#7
'''
g = np.random.randint(10,30,5)
print(g)
'''
#8
'''
h = np.random.randn(10)
print(h)
'''
#9
'''
i = np.random.randint(10,50,15).reshape(3,5)
print(i)
'''
#10
'''
j = np.random.randint(10,50,15).reshape(3,5)
rowTotal = j.sum(axis = 1)
colTotal = j.sum(axis = 0)
print(j,rowTotal,colTotal)
'''
#11
'''
k = np.random.randint(0,100,10)
Max= np.max(k)
Min= np.min(k)
arAverage= np.average(k)
print(k,Max,Min,arAverage)

'''
#12
'''
print(k.argmax(),k.argmin())
'''
#13
'''
l = np.arange(10,20)
print(l[:3])
'''
#14
'''
m = np.arange(10,20)
print(m[::-1])
'''
#15
'''
print(i[0])
'''
#16
'''
print(i[1,2])
'''
#17
'''
print(i[:,0])
'''
#18
'''
print(i**2)


