#!/usr/bin/env python
# coding: utf-8

# In[3]:


def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)


# In[4]:


factorial(10)


# In[5]:


factorial(2)


# In[6]:


factorial(3)


# In[11]:


data=[1,2,4,6,7,8,9,10,15,16,17,18,19,20,22,26,28,29]


# In[9]:


def binary_search(data, target, low, high):
    if low >high:
        return False
    else:
        mid=(low+high)//2
        if target==data[mid]:
            return True
        elif target<data[mid]:
            return binary_search(data, target, low, mid-1)
        else: 
            return binary_search(data, target, mid+1, high)


# In[12]:


binary_search(data, 15, 1, 29)


# 음 다시해보기

# In[13]:


origindata = [10,5,30,40,2,4,9,80,44,23,3]
copydata=[0,0,0,0,0,0,0,0,0,0,0]


# In[14]:


print(origindata)


# In[15]:


for i in range(0, len(origindata)):
    copydata[i]= origindata[i]
print(copydata)


# good.?!

# In[18]:


def find_max(data):
    biggest = data[0]
    for val in data:
        if val > biggest:
            biggest = val
    return biggest
data=[10, 5, 30, 40, 2, 4, 9, 80, 44, 23, 3]
print(find_max(data))


# 1. val 부분이 뭔지 모르겠음

# In[23]:


data = ['A', 'B', 'C', 'D']
def insert_data(position, name):
    if position < 0 or position >len(data):
        print("out of range...")
        return
    data.append(None)
    KLen = len(data)
    
    for i in range(KLen-1, position, -1):
        data[i] = data[i-1]
        data[i-1]=None
        
    data[position] = name

print(data)
insert_data(2, 'B2')
print(data)
insert_data(1,'A2')
print(data)


# data = ['A', 'B', 'C', 'D', None, None]
# for i in range(5, 3, -1):
#     data[i] = data[i-1]
#     data[i-1]=None    
#     print(data)
# //연습해봄
# 

# 1. return 이 아무것도 없는것
# 2. data.append(None)부분쓰는 이유
# 3. KLen을 저렇게 자료 정의를 c와 달리 타입 정의 없이 막해도 되는건지
# 4. for문 익혀야할듯
# 5. 다시 읽어뵉

# In[9]:


data  = ['A', 'B', 'C', 'D']
def delete_data(position):
    if position < 0 or position >len(data):
        print("out of range...")
        return
    KLen = len(data)
    data.append(None)
    print("//", data)
    
    for i in range(position+1, KLen):
        data[i-1] = data[i]
        data[i]=None
        
    del(data[KLen-1])

print(data)
delete_data(1)
print(data)
delete_data(2)
print(data)    


# 1. 위의 insert_Data와 다르게 왜 KLen 정의를 먼저 하는 것인가
# 2. for문의 변화
# 3. 굿?

# In[26]:


inData = [10,5,30,40,2,4,9]
outData = [0,0,0,0,0,0,0]

pre_bound=0

for i in range(1, len(inData)):
    low_bound = 100
    
    for j in range(1, len(inData)):
        
        if inData[j]>pre_bound:
            if inData[j]<low_bound:
                low_bound = inData[j]
    outData[i]= low_bound
    pre_bound = low_bound
print(outData)


# 1. 왜 bound문장 끝에 세미콜론을 붙이셨을까
# 2. inData[]에서 0보다 작을 때는 정의를 안 해도 되는걸까, lowBound도 100이하로 잡는 이유 마찬가지
# 3. 반복문 보는 연습 해야될듯 복잡함
# 

# In[36]:


stack = [None,None,None,None,None]
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1


# 1. 그냥ㅁ 뭔지 모르겠음

# In[14]:


SIZE = 5
stack = ['A','B','C','D','E']
top=4

def isStackFull():
    global SIZE, stack, top
    
    if (top>=SIZE-1):
        return True
    else:
        return False

print("check the full statement?", isStackFull())


# 1. global은 전역그거 만드는 것인가?
# 2. 이거는 어디다 써먹는 함수인지

# In[31]:


def isStackFull():
    global SIZE, stack, top
    
    if (top>=SIZE-1):
        return True
    else:
        return False
def push(data):
    global SIZE, stack, top
    if(isStackFull()):
        print("Stack is full")
        return
    top+=1
    stack[top]= data
    
SIZE = 5
stack = ['A','B','C','D', None ]
top=3

print(stack)
push('E')
print(stack)
push('F')


# 1. 대충 이해하겠음 
# 2. 굿

# In[33]:


def isStackFull():
    global SIZE, stack, top
    
    if (top>=SIZE-1):
        return True
    else:
        return False
def push(data):
    global SIZE, stack, top
    if(isStackFull()):
        print("Stack is full")
        return
    top+=1
    stack[top]= data
def isStackEmpty():
    global SIZE, stack, top
    if(top==-1):
        return True
    else:
        return False
SIZE = 5
stack = [None for _ in range(SIZE) ]
top=-1

print("check stack empty statement : ", isStackEmpty())


# 1. global을 저리 매번 정의해줘야 하는 지(함수정의 때마다)
# 2. -1이 top이면 왜 빈것인가: 그냥 0이라고 하면 안되나
# 3. 저기 None for 은 뭘 의미하는 것인지

# In[37]:


def isStackFull():
    global SIZE, stack, top
    
    if (top>=SIZE-1):
        return True
    else:
        return False
def push(data):
    global SIZE, stack, top
    if(isStackFull()):
        print("Stack is full")
        return
    top+=1
    stack[top]= data
def isStackEmpty():
    global SIZE, stack, top
    if(top==-1):
        return True
    else:
        return False
def pop():
    global SIZE, stack, top
    if(isStackEmpty()):
        print("Stack is Empty/...")
        return None
    data = stack[top]
    stack[top]= None
    top-=1
    return data
SIZE = 5
stack = ['A', None,None,None,None]
top=0

print(stack)
retData = pop()
print("return data -> ", retData)
print(stack)
retData = pop()


# In[ ]:





# 

# operation1: copy input numbers to originData (program takes input operations from a user, multiple data)

# In[68]:


originData = [int(x) for x in input("숫자를 입력하세요: ").split()]

print("입력된 숫자들:", originData)


# operation2: sorting the numbers (data should store the form of list ..[1, 2, 3, 4, ..]

# In[69]:


print("before ---> ", originData)

outData=[None for _ in range(len(originData))]

def find_max(data):
    biggest=data[0]
    for i in range(len(data)):
        if biggest<=data[i]:
            biggest=data[i]
    return biggest

prebound = 0

for i in range(len(originData)):
    lowbound=find_max(originData)
    for j in range(len(originData)):
        if originData[j]>prebound:
            if originData[j]<=lowbound:
                lowbound=originData[j]
    outData[i]=lowbound
    prebound = lowbound
print("sorted numbers ---> ",outData)
  


# operation3: copy the result to destData

# In[70]:


destData = [None for _ in range(len(outData))]
for i in range(len(outData)):
    destData[i]=outData[i]


# operation4: print out the sorted list

# In[71]:


print(destData)

