# Highest in the level
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def largestValuesInTreeRows(t):
    if t == None:
        return []
    values = [t]
    ans = []
    while len(values) > 0:
        
        i = 0
        temp = []
        tans = []
        while(i < len(values)):
            if values[i] != None:
                tans.append(values[i].value)
                temp.append(values[i].left)
                temp.append(values[i].right)
            i += 1
        if len(tans) > 0:
            ans.append(max(tans))
        values = temp
    return ans
