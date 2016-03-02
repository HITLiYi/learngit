#/usr/bin/env python
#coding:utf-8
'''
二叉树生成与深度遍历
'''
__author__ = 'daged'
class TreeNode(object):
    def __init__(self,root=0,left=None,right=None):
        self.root=root
        self.left,self.right=left,right
class Traversal(object):
    def __init__(self):
        self.traverse_path=list()
    def preorder(self,rootnode):
        if rootnode:
            self.traverse_path.append(rootnode.root)
            self.preorder(rootnode.left)
            self.preorder(rootnode.right)
    def inorder(self,rootnode):
        if rootnode:
            self.inorder(rootnode.left)
            self.traverse_path.append(rootnode.root)
            self.inorder(rootnode.right)
    def postorder(self,rootnode):
        if rootnode:
            self.postorder(rootnode.left)
            self.postorder(rootnode.right)
            self.traverse_path.append(rootnode.root)
n1=TreeNode(1)
n2=TreeNode(2,n1,0)
n3=TreeNode(3)
n4=TreeNode(4)
n5=TreeNode(5,n3,n4)
n6=TreeNode(6,n2,n5)
n7=TreeNode(7,n6,0)
n8=TreeNode(8)
root=TreeNode('root',n7,n8)
bt=Traversal()
bt.preorder(root)
print(bt.traverse_path)
bt.traverse_path=[]
bt.inorder(root)
print(bt.traverse_path)
bt.traverse_path=[]
bt.postorder(root)
print(bt.traverse_path)