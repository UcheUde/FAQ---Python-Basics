
print("Python" "is"  "amazing")

# li=[10,20,30,40]              #•••SWAPPING ELEMENTS•••5:pop#
# first=li.pop(0)
# last=li.pop(-1)
# li.insert(0,last)
# li.append(first)
# print(li)

# li=[10,20,30,40]            #•••SWAPPING ELEMENTS•••4:*operand#
# start,*middle,end=li
# li=end,*middle,start
# print(li)

# li=[10,20,30,40]          #•••SWAPPING ELEMENTS•••3:TUPLE#
# n=(li[3],li[0])
# li[0],li[3]=n
# print(li)

# li=[10,20,30,40]          #•••SWAPPING ELEMENTS•••2#
# temp=li[3]
# li[3]=li[0]
# li[0]=temp
# print (li)
#
# li=[10,20,30,40]          #•••SWAPPING ELEMENTS•••1#
# li[0],li[3]=li[3],li[0]
# print (li)


# li=(3,24,44,72,81,10,48,22)   #•••LENGTH OF A LIST•••#
# count=0
# for i in li:
#     count=count + 1
# print ("The length of the list is:", count)
# print (len(li))


# l=[]           #•••MAX & MIN ELEMENTS••• RANDOM NUMBERS#
# from random import randint
# for i in range (5):
#     l=l+[randint(1,100)]
# print (l)
# max=l[0]
# min=l[0]
# n=len(l)
# for i in range (1,n):
#     if l[i]>max:
#         max=l[i]
# print ("The maximum element is:", max)
# for i in range (1,n):
#     if l[i]<min:
#         min=l[i]
# print ("The minimum element is:", min)

# l=[]         #•••MAX & MIN ELEMENTS••• INPUT NUMBERS#
# for i in range (0,3):
#     num=int(input("Enter a number: "))
#     l.append(num)
# print (l)
# max=l[0]
# min=l[0]
# n=len(l)
# for i in range (1,n):
#     if l[i]>max:
#         max=l[i]
# print ("The maximum element is:", max)
# for i in range (1,n):
#     if l[i]<min:
#         min=l[i]
# print ("The minimum element is:", min)

# num=(10,50,22,64,30)    #•••MAX & MIN ELEMENTS•••#
# listNum=list(num)
# print (listNum)
# max=listNum[0]
# min=listNum[0]
# n=len(listNum)
# for i in range (1,n):
#     if listNum[i]>max:
#         max=listNum[i]
# print (max)
# for i in range (1,n):
#     if listNum[i]<min:
#         min=listNum[i]
# print (min)


# arr=(1,2,3,4,2)      #••••••SUM, ADD & SUB ELEMENTS IN/TO ARRAY•••••#
# print(sum(arr))     #sum
# print(sum(arr,10))  #add
# print(sum(arr,-7))  #sub


# n1=0                #••••••FIBONACCI SERIES•••••#
# n2=1
# for i in range (2,10):
#     sum=n1 + n2
#     n1=n2
#     n2=sum
#     print(sum)


# def factorial(n):                    #•••FACTORIAL•••#
#     if n<=0:
#         return 1
#     else:
#         return n * factorial(n-1)
#     # return 1 if n<=0 else n * factorial(n-1)
# n=int(input("Enter a number: "))
# print ("The factorial of", n, "is", factorial(n))

# num=int(input("Enter a number: "))    #•••FACTORIAL•••#
# factorial=1                           #•••FACTORIAL: multiples of the preceeding numbers•••#
# if num<=0:
#     print ("Factorial does not exist!")
# else:
#     for i in range (1,num+1):
#         factorial = factorial*i
#     print ("The factorial of", num, "is", factorial)


# num=int(input("Enter a number:", ))     #•••FIND PRIME NUMBERS•••#
# count=0                                 #•••PRIME NUMBERS:numbers divisible by 1 and itself•••#
# if num>1:
#     for i in range (1,num+1):
#         if (num%i)==0:
#             print (i)
#             count=count+1
#     if count==2:
#         print(num, "is prime")
#     else:
#         print(num, "is NOT prime")


# x=int(input("Enter a number:", ))
# for i in range(1,x):               #•••numbers divisible by num•••#
#     if x%i==0:
#         print (i)


# n1=10
# n2=20
# temp=n1       #••••SWAPPING NUMBERS 1••••#
# n1=n2
# n2=temp
# n1,n2=n2,n1    #•••••SWAPPING NUMBERS 2•••••#
# print(n1,n2)