import sys
#迭代器
#list=[1,2,3,4]
#it=iter(list) #创建迭代器对象
#print(iter(it)) #输出迭代器的下一个对象
#for x in it:
    #print(x,end="")
'''用next的情况
print("er")
while True:
    try:print(next(it))
    except StopIteration:
        sys.exit()
'''

#生成器
def fibonacci(n):
    a,b,counter=0,1,0
    while True:
        if(counter>n):
            return
        yield a
        a,b=b,a+b
        counter+=1
f=fibonacci(10)
while True:
    try:
        print(next(f),end="")
    except StopIteration:
        sys.exit()
