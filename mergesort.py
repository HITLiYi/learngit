#/usr/bin/env python
#coding:utf-8

class Sort:
        def  mergesort(self,alist):
	        if len(alist)<=1:
			return alist
		mid=len(alist)//2
		left=self.mergesort(alist[:mid])
		print('left='+str(left))
		right=self.mergesort(alist[mid:])
		print('right='+str(right))
		return self.mergesortedArray(left,right)
	def mergesortedArray(self,A,B):
	        sortedArray=[]
		l=0
		r=0
		while l<len(A) and r< len(B):
		        if A[l]<B[l]:
				sortedArray.append(A[l])
				l+=1
			else:
			        sortedArray.append(B[r])
			        r+=1
		sortedArray+=A[l:]
		sortedArray+=B[r:]
		return sortedArray
unsortedArray=[6,5,3,1,8,7,2,4]
merge_sort=Sort()
print(merge_sort.mergesort(unsortedArray))