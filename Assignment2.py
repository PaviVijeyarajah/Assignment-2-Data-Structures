#pip install playsound==1.2.2
from playsound import playsound
import random

def mergeSort(product_id):
    first=[]
    last=[]
    if len(product_id) > 1:

        mid=len(product_id)/2
        for i in range (len(product_id)):
            if i < mid:
                first.append(product_id[i])
            else:
                last.append(product_id[i])

        mergeSort(first)
        mergeSort(last)

        t1=0
        t2=0
        t3=0
        
        while t1 < len(first) and t2 < len(last):
            if first[t1] <= last[t2]:
                product_id[t3] = first[t1]
                t1 += 1
            else:
                product_id[t3] = last[t2]
                t2 += 1
            t3 += 1
            
        while t1 < len(first):
            product_id[t3] = first[t1]
            t1 += 1
            t3 += 1

        while t2 < len(last):
            product_id[t3] = last[t2]
            t2 += 1
            t3 += 1
            
        playsound('bell1.wav')
        print(product_id)
        
product_id = [11,1,30,2,51,6,29,7,67,15,118,4,89,23]
new=[]
user=input("Do you wish to create your own array or use the default for sorting\n Type 'new' to use new one\n Type 'default' for the default\n Type 'exit' to leave\n")
if user == "default":
    print()
    mergeSort(product_id)
if user == "new":
    num=int(input("Select the number of values you want in your array: "))
    for i in range(num):
        new.append(random.randrange(1,50))
    print("This is your array\n",new)
    print()
    mergeSort(new)
if user == 'exit':
    print("Bye")