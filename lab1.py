word="marwan is taking course with iti and iti is great"
count=0
for w in word.lower():
    if w in ["a","e","o","i",'u']:

        count+=1
print(count)
#words=[]
#for x in range(4):
#    w = input("Please enter "+ str(x) + " word ")
#    print(w)
#    words.append(w)

#words.sort()
#print(words)
#c=0
#word=word.split()
#for w in word:
 #   if w.lower()=="iti":
  #      c+=1
#print(c)
#new_word=""
#for w in word:
#    if w not in ["a","e","o","i",'u']:
#        print(w)
#        new_word += w
#print(new_word)
occ=[] # lost of t occurences
#for i,c in enumerate(word.lower()):
#    if c == "i":
#        occ.append(i)
#print(occ)
def generate_multiplication_table(num):
    table = []  # List to store the multiplication table

    for multiplicand in range(1, num + 1):
        r = [multiplicand * multiplier for multiplier in range(1, multiplicand + 1)]
        table.append(r)

    return table
x=generate_multiplication_table(3)

h=4
for i in range(1, h + 1):
        space = ' ' * (h - i)  # Calculate spaces for right alignment
        star = '*' * i
        print(space + star)
