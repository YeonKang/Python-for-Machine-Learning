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

#list complrehension

result = [i for i in range(10)]
print(result)

