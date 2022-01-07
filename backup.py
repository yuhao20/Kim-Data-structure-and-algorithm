#P23

import time

def test1(n):
    start=time.time()
    lst=[]
    for i in range(n*1000):
        lst=lst+[i]
    end=time.time()
    print('test1运行时间为'+str(end-start))
    return lst

def test2(n):
    start=time.time()
    lst=[]
    for i in range(n*1000):
        lst.append(i)
    end=time.time()
    print('test2运行时间为'+str(end-start))
    return lst

def test3(n):
    start=time.time()
    lst=[i for i in range(n*1000)]
    end=time.time()
    print('test3运行时间为'+str(end-start))
    return lst

def test4(n):
    start=time.time()
    lst=list(range(n*1000))
    end=time.time()
    print('test4运行时间为'+str(end-start))
    return lst

test1(100)
test2(100)
test3(100)
test4(100)

#时间 1>>2>3>4



#P68
#注：文字语义中第i个 对应顺序表中第i-1个

class MyList:
    
    def __init__(self,size):
        self.size=size
        self.show=[]
        self.num=0
        
    def is_empty(self):                 #判断是否空
        if self.num==0:
            print('空顺序表！')
            return 1
        else:
            return 0
    
    def _is_full(size,num):             #判断是否满
        if size==num:
            print('顺序表已满！')
            return 1
        else:
            return 0
        
    def Len(self):                      #判断长度
        return self.num
    
    
    
    def Prepend(self,elem):             #增加元素三类操作
        
        if MyList._is_full(self.size,self.num):
            print('增加失败')
        else:
            self.show.insert(0,elem)
            self.num+=1
            
        
    def Append(self,elem):
        
        if MyList._is_full(self.size,self.num):
            print('增加失败')
        else:
            self.show.append(elem)
            self.num+=1
        
    def Insert(self,elem,i):
        
        if i>=self.size:
            print('索引超出范围！')
            raise IndexError
        elif  MyList._is_full(self.size,self.num):
            print('插入失败')          
        else:
            self.show.insert(i-1,elem)     #把元素插入到第i个位置   有点小瑕疵，因为中间没有0
            self.num+=1
    
    
    def Del(self,i):                     #删除元素三类操作
        if self.num==0:
            print('空顺序表！')
        else :
            self.show.pop(i-1)
            self.num-=1
            
            
    def Del_first(self):
        if self.num==0: 
            print('空顺序表！')
        else :
            self.show.pop(0)
            self.num-=1
            
        
    def Del_last(self):
        if self.num==0:
            print('空顺序表！')
        else :
            self.show.pop()
            self.num-=1
            
            
    def Search(self,elem):                     #索引
        for i in range(self.num):
            if self.show[i]==elem:
                return i+1
            else:
                pass
        print('未找到此元素！')
        return 0
    
#示例    
mylist=MyList(5)
mylist.is_empty()
mylist.Len()
mylist.Prepend('start')
mylist.Append('end')
mylist.Insert('a',1)
mylist.show
mylist.num
mylist.Search('a')
mylist.Del_first()
mylist.Del_last()


#P100
#Josephus(约瑟夫)问题 顺序表  位置均-1！！！初始 旋转 都是-1
#两个减一意义不一样 前者是位置转成数组下标要-1 后者是死了一个后面下标前移所以相对移动也-1
#test1耗时：15min写完，调试半小时，最后还是参考了答案，+1-1傻傻分不清
#n把椅子，从第k个人开始，m一循环出一个人

#step1 建表
#step2 初始命运指针
#step3 旋转指针
#step4 剔除
#step5 跳到step3

def Josphus_L(n,k,m):
    people=[]
    for i in range(n):
        people.append(i+1)#初始人序号,即people=[1,2,3,...,n]
    
    num=n   #num表示在场人数
    j=k-1     #j为指针                    #init j=k    #从第几个索引的角度看而不是第几个人的角度，会存在1的差距
    print(people)
    
    while num>0:
        #算出踢掉人的序号并打印
        j=(j+m-1)%num                     #init j=(j+m-1)%num
        
        die=people.pop(j)                 #init pop(j-1)           可能是不用索引下标那就是1到...对应不上了
        print(str(die)+'\n')
        #每次踢掉一个人
        num=num-1
        
        
    print(people)   
    
Josphus_L(7,2,3)

#Josephus(约瑟夫)问题 循环链表 考察全面

#新建结点
class Node:
    def __init__(self,elem,next_=None):
        self.elem=elem
        self.next=next_

#新建循环单链表
class LClist:
    def __init__(self):
        self._rear=None
        
    def is_empty(self):
        return self._rear is None
    
    def prepend(self,elem):
        #空的，直接建立
        p=Node(elem)
        #空的，直接建立
        if(self._rear is None):
            p.next=p
            self._rear=p
        
        #非空，+元素 移动rear
        else:
            p.next=self._rear.next
            self._rear.next=p
            
    def append(self,elem):
        self.prepend(elem)
        self._rear=self._rear.next
    
    def pop(self):                          #从rear的下一个开始删除
        #空了，报错
        if self._rear is None:
            print('空链表，不可删除操作！')
        p=self._rear.next   #相当于头指针  
        
        #单个Node
        if self._rear is p:
            self._rear=None
            return p.elem
        
        #多个Node
        else:
            self._rear.next=p.next
            return p.elem
        
#约瑟夫问题循环链表解法
class Josphus_LC(LClist):
    
    #转m个删掉一个节点
    def turn(self,m):
        for i in range(m):
            self._rear=self._rear.next
    
    def __init__(self,n,k,m):
        LClist.__init__(self)
        for i in range(n):
            self.append(str(i+1))
        
        self.turn(k-1)
        
        while not self.is_empty():
            #转起来
            self.turn(m-1)
            #删除
            print(self.pop())
            
    
mytest1=Josphus_LC(7,2,3)




#正则表达式

#match从开头开始；search任意位置 包含match方法；split用匹配串分割原串；
#findall找到所有匹配串(结果是若干相同的串，实际意义不大，不过可以统计有多少匹配的)
#使用match.group()查看内容.span()查看范围 .start .end查看起点终点
#sub()用于替换 re.sub(pattern,repl,string,count=0,flags=0)

#总共14个元字符

#  .可以匹配任意字符
# [0-9]//[a-z]  匹配范围数
# (xxx)?  匹配0或1次   ()* 匹配>=0次    ()+ 匹配>1次
# {m,n}重复m到n次
# * + ？{m,n} 都采取贪婪匹配规则

#a|b|c等价于[abc]

import re

#compile形成模板
r1=re.compile('66lao')

r1.match('66lao 6766lao!').group()
r1.search('ni shi yi ge 66lao 6766lao!').span()
r1.split('ni shi yi ge 66lao 6766lao!')
r1.findall('ni shi yi ge 66lao 6766lao!')


#P133 T5 b)
import re

#htmltest文本对应源代码网址;
#view-source:https://so.lenovo.com.cn/

with open(r'C:\Users\King\Data structure and algorithm\htmltest.txt','rb') as f:
    content=f.read()
    
#new_content=str(content).split(r'\r\n')   #不好使
new_content=str(content).split(' ')  #用空格分

pattern1=re.compile('"(https:)?/{2}.*?\.[a-z]{2,4}(")')

#(https:)? 0或1个http:
#/{2} 对应//
#.*? 非贪婪无限多字符
# \.[a-z]{2,4}对应 .加上2到4位字母 例如 .cn .com等

 
tar1_list=[]    #保存提取后的网址列表

for each in new_content:
    try:
        tar1_list.append(pattern1.search(each).group())
    except:
        pass
    
tar1_list

