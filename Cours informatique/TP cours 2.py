#Exercices pour cours 1
#Verifier biopython pour comment lire des fichiers FASTA

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



x = 10
while x < 25:
    print(x)
    x = x+1
print('all done')

def give_exponent(numList):
    lst = []
    for i in numList:
        try:
            lst.append(i**2)
            print(lst)
        except:
            print("""Please input a list of only integers""")
    return(lst)

print(a = give_exponent([1,2,3,4,"Bad",5]))