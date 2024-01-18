#---Problem: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#------------------
#------Answer------
#------------------
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        else:
            tree = []
            currNodes = [root]
            nextNodes = []
            currCoords = [[0,0]]
            nextCoords = []
            while True:
                for i in range(len(currNodes)):
                    if currNodes[i] is not None:
                        tree.append([currNodes[i].val, currCoords[i]])
                    if currNodes[i].left is not None:
                        nextNodes.append(currNodes[i].left)
                        nextCoords.append(
                            [currCoords[i][0]+1, currCoords[i][1]-1]
                        )
                    if currNodes[i].right is not None:
                        nextNodes.append(currNodes[i].right)
                        nextCoords.append(
                            [currCoords[i][0]+1, currCoords[i][1]+1]
                        )
                if len(nextNodes) == 0:
                    break
                else:
                    currNodes = nextNodes
                    nextNodes = []
                    currCoords = nextCoords
                    nextCoords = []
        tree.sort(key = lambda sort: (sort[1][1], sort[1][0], sort[0]))
        ans = {}
        for nodes, coords in tree:
            ans.setdefault(coords[1], []).append(nodes)
        return ans.values()
#------------------
#------Answer------
#------------------

#-------------------
#------Testing------
#-------------------
def build_tree(nodes, index=0):
    if index < len(nodes):
        if nodes[index] is not None:
            root = TreeNode(nodes[index])
            root.left = build_tree(nodes, 2 * index + 1)
            root.right = build_tree(nodes, 2 * index + 2)
            return root
    return None

#Input
nodes = [3, 9, 20, None, None, 15, 7]

# Build the binary tree
root = build_tree(nodes)

# Create an instance of the Solution class
solution_instance = Solution()

# Call the verticalTraversal method on the Solution instance
result = solution_instance.verticalTraversal(root)

# Print the result
print(result)
#-------------------
#------Testing------
#-------------------