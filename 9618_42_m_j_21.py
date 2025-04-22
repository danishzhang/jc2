# Q1(a)
class node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node    

# Q1(b)
linkedList = [node(1,1), node(5,4), node(6,7), node(7,-1),
              node(2,2), node(0,6), node(0,8), node(56,3),
              node(0,9), node(0,-1)]
startPointer = 0
emptyList = 5

# Q1(c)

def outputNodes(linkedList, itempointer):
    while itempointer != -1:
        print(linkedList[itempointer].data, linkedList[itempointer].next_node)
        itempointer = linkedList[itempointer].next_node

outputNodes(linkedList, startPointer)
