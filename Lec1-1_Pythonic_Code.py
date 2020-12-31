#basic code

alphabet = ["a","b","c","d","e"]
result = ""

for s in alphabet:
    result += s
print(result)

#pythonic code

alphabet = ["a","b","c","d","e"]
result = "".join(alphabet)
print(result)

#split string

items = 'zero one two three'.split()
print(items)

example = 'python,c++,java'
print(example.split(","))

#split string and unpacking

example = 'python, c++, java'
a,b,c = example.split(",")
print(a,b,c)

#for loop + append

result = []

for i in range(10):
    result.append(i)
print(result)

#list Complrehension

result = [i for i in range(10)]
print(result)

result = [i for i in range(10) if i % 2 == 0]
print(result)

#Nested For loop

word_1 = "Hello"
word_2 = "World"
result = [i+j for i in word_1 for j in word_2]
print(result)

#Nested For loop + if

case_1 = ["A","B","C"]
case_2 = ["D","E","A"]

result = [i+j for i in case_1 for j in case_2]
print(result)

result = [i+j for i in case_1 for j in case_2 if not(i==j)]
result.sort()
print(result)

#split + list Comprehension

words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)

stuff = [[w.upper(),w.lower(),len(w)] for w in words]

for i in stuff:
    print(i)

#for loop + zip

alist = ['a1','a2','a3']
blist = ['b1','b2','b3']

for a,b in zip(alist,blist):
    print(a,b)

#list comprehension + zip

a,b,c = zip((1,2,3),(10,20,30),(100,200,300))
print(a,b,c)
print([sum(x) for x in zip((1,2,3),(10,20,30),(100,200,300))])

#enumerate + zip

alist = ['a1','a2','a3']
blist = ['b1','b2','b3']

for i,(a,b) in enumerate(zip(alist,blist)):
    print(i,a,b)

#lambda function

def f(x,y):
    return x+y
print (f(1,4))

f = lambda x,y:x+y
print(f(1,4))

f = lambda x:x/2
print(f(3))

f = lambda x:x**2
print(f(3))
print((lambda x:x+1)(5))

#map with lambda

ex = [1,2,3,4,5]
print(list(map(lambda x: x+x, ex)))
print((map(lambda x: x+x, ex)))

f = lambda x: x ** 2
print(map(f, ex))
for i in map(f, ex):
    print(i)

result = map(f, ex)
print(result)
print(next(result))

import sys
sys.getsizeof(ex)
sys.getsizeof((map(lambda x: x+x, ex)))
sys.getsizeof(list(map(lambda x: x+x, ex)))

#reduce with lambda

from functools import reduce
print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))

def factorial(n):
    return reduce(
            lambda x, y: x*y, range(1, n+1))

print(factorial(5))