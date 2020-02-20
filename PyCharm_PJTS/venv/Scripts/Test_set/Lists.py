#--------------------------- СПИСКИ  -----------------
l = []
lis = [1, 56, 'x', 34, 2.34, ['S', 't', 'r', 'o', 'k', 'a']]
print (lis)

a = [a + b for a in 'list' if a != 's' for b in 'soup' if b != 'u']
print (a)

l.append (23)
l.append (34)
b = [24, 67]
l.extend (b)