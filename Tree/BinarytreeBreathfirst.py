#breathfirst traversing
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def traverseTree(t):
    if t == None:
        return []
    values = [t]
    ans = []
    while len(values) > 0:
        i = 0
        temp = []
        while(i < len(values)):
            if values[i] != None:
                ans.append(values[i].value)
                temp.append(values[i].left)
                temp.append(values[i].right)
            i += 1
        values = temp
    return ans
    