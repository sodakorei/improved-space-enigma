import sys
input = sys.stdin.readline

def preorder(cur):
    if cur != '.':
        print(cur, end='')
        preorder(tree[cur][0])
        preorder(tree[cur][1])
    return

def inorder(cur):
    if cur != '.':
        inorder(tree[cur][0])
        print(cur, end='')
        inorder(tree[cur][1])
    return

def postorder(cur):
    if cur != '.':
        postorder(tree[cur][0])
        postorder(tree[cur][1])
        print(cur, end='')
    return

n = int(input())
tree = dict()
for _ in range(n):
    parent, left, right = input().strip().split()
    tree[parent] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')