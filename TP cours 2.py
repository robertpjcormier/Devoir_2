#Exercices pour cours 1

#Integers + floats

x = 5
y = 4
print(x + 6)
print(x * 2)
print(x - y)
print(y / 2)

#Booleans

a = 10
b = 12
c = 0
print(a > 0)
print(b < 10)
print(a == b)
print(True or False)
print(True and False)

# Les Strings

s = 'ACCGTGCATATA'
print(s + 'TTCCG')

g = 'AACCGGTT'
print(g[0])
print(g[-1])
print(g[0:4])
print(g[2:-3])

# Tuples

t = (1,"ACGT", 24.55)
print(t)
print(t[1])

#Lists

l = ["ACC", "TGA", "GAT"]
l.pop()
print(l)
l.append("AAA")
l.remove("TGA")
print(l)

#Dictionnaire

d = {"CCU":"P", "AUG":"M", "AGA":"R", "UGA":"Stop"}
print(d["AUG"])

#Commande de base et indentations

x = 44
y = 33
if x > y:
    print("x is greater")
else:
    print("x is smaller or equal")



