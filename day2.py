def generatelist(len,start):
    lst=[]

    for x in range(len):
        lst.append(start)
        start+=1
    return lst
def div(num):
    if num%3==0 and num%5==0:
        return "fuzz buzz"
    elif num%3==0:
        return "fuzz"
    elif num%5 == 0:
        return "buzz"
    else:
        return "Noz"
print(div(105))

def rstr(word):
    rword=""
    for c in word:
        rword = c +rword
    return rword
print(rstr("maro"))

def vaildate():
    while True:
        name=input("Please enter your name")
        if len(name)<1:
            name = input("Please enter your name again")
        else:
            break
    while True:
        email=input("Please enter your email")
        if len(email.split("@") ) !=2:
            input("Please enter your email again")
        else:
            break
def alphaorder(word):
    long=""
    cur=word[0]
    for i in range(1,len(word)):
        if word[i]>= word[i-1]:
            cur+=word[i]
        else:
            if len(cur)>len(long):
                long=cur
            cur=word[i]
    if len(cur)>len(long):
        long=cur
    return long

#print(alphaorder("abcbcefgh"))


def readnums():
    lst=[]
    while True:
        num=input("Please enter number ")
        if num.lower() =="done":
            break
        try:
            inum=int(num)
        except:
            print("Please enter a number")
            continue
        lst.append(inum)
    print(f"Sum is {sum(lst)}" )
    print(f"Average is{ sum(lst)/len(lst)} ")
    print(f"Count is {len(lst)}" )
#readnums()
import random

def guessgame(words):
    randomword=random.choice(words)
    c = input("Enter a random char ")
    for _ in range(7):
        if c in randomword:

            print("Win")
            break
        else:
            print("try another char")
            c = input("Enter a random char ")
    print("you lose")
guessgame(["marwan","ahmed", "sayed","nouran","esraa"])

