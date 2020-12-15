n=int(input("enter number of words"))

words=[]
for i in range(1,n+1):
    x=(input("enter word"))
    words.append(x)

print(words)



def Stringdel(words):
    flag = 0
    v = 0
    while v<=100:

        words=list(map(lambda a:a[1:],words))
        v+=1
        print(words)

        for i in words:

            if words.count(i)>1:
                print(v,'fff')
                flag=1
                break
            elif len(i)==0:
                flag=1
                print(v,'sss')
                break
        if flag==1 and v%2==0:
            print("watson")
            break
        elif flag==1 and v%2!=0:
            print("sherlock")
            break
Stringdel(words)