import random

a1 = input("select the title:")

a = input("select 1:")
b = input("select 2:")
c = input("select 3:")
d = input("select 4:")
e = input("select 5:")
f = input("select 6:")

g = random.choice([a,b,c,d,e,f])

print(str(a1) + str(g))


