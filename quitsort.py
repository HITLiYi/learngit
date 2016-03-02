#/usr/bin/env python
#coding:utf-8
'''
快速排序算法
'''
__author__ = 'daged'
class Quitsort():
    '''
    非原地快排，遍历数组，比参考值小的放左边，大的放右边，循环迭代
    '''
    def qsort1(self,alist):
        print(alist)
        if len(alist)<=1:
            return alist
        else:
            pivot=alist[0]
            return (self.qsort1([x for x in alist[1:] if x <pivot])+\
                    [pivot]+\
                    self.qsort1([x for x in alist[1:] if x >pivot]))
    '''
    原地快排，遍历数组，选定参考值，依然是比参考值小的先取出，但序列并不迭代到最底层，而是将序列每次更改传输到下一层，最终在底层输出
    '''
    def qsort2(self,alist,l,u):
        print(alist)
        if l>=u:
            return alist
        m=l
        for i in range(l+1,u+1):
            if alist[i]<alist[l]:
                m+=1
                alist[m],alist[i]=alist[i],alist[m]
        alist[m],alist[l]=alist[l],alist[m]
        self.qsort2(alist,l,m-1)
        self.qsort2(alist,m+1,u)
    '''
    双向快排，左右向中遍历数组，一大一小交换数据
    '''
    def qsort3(self,alist,lower,upper):
        print(alist)
        if lower>=upper:
            return
        pivot=alist[lower]
        left,right=lower+1,upper
        while left<=right:
            while left<=right and alist[left]<pivot:
                left+=1
            while left<=right and alist[right]>=pivot:
                right -=1
            if left>right:
                break
            alist[left],alist[right]=alist[right],alist[left]
        alist[lower],alist[right]=alist[right],alist[lower]
        self.qsort3(alist,lower,right-1)
        self.qsort3(alist,right+1,upper)


unsortedqueue=[6,5,3,1,8,7,2,4]
m=Quitsort()
print(m.qsort3(unsortedqueue,0,len(unsortedqueue)-1))
