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