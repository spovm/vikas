n=int(input("enter the value"))
sum=0
while(n>0):
    a=n%10
    sum=sum+a
    n=n//10
    print("the sum of total digits is",sum)
