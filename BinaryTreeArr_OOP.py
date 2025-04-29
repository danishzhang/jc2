# 1 a i
class Node:
    def __init__(self, Data1):
        #DECLARE Data, LeftPointer, RightPointer : INTEGER
        self.__LeftPointer = -1 
        self.__Data = Data1
        self.__RightPointer = -1 

# 1 a ii
    def GetLeft(self):
        return self.__LeftPointer
    def GetRight(self):
        return self.__RightPointer
    def GetData(self):
        return self.__Data
    
# 1 a iii
    def SetLeft(self, num):
        self.num = num
    def SetRight(self, num):
        self.num = num
    def SetData(self, data):
        self.data = data

# 1 b i
class TreeClass:
    def __init__(self):
        #DECLARE Tree: ARRAY[0:19] OF Node
        # DECLARE FirstNode, NumberNodes : INTEGER
        self.__Tree = [Node for i in range(20)]
        self.__FirstNode = -1
        self.__NumberNodes = 0

        
# 1 b ii
    def InsertionNode(self, NewNode): # NewNode is of type Node
        if self.__NumberNodes == 0:
            self.__Tree[self.__NumberNodes] = NewNode
            self.__NumberNodes =+ 1
            self.__FirstNode = 0
        else:
            self.__Tree[self.__NumberNodes] = NewNode # Newnode represents [LeftPointer, Data, RightPointer] 
            
            while True:
                self.__NumberNodes =+ 1
                if self.__Tree[self.__FirstNode].GetData() > NewNode.GetData(): # Use GetData() to get the value inside the NewNode
                    if self.__Tree[self.__FirstNode].GetLeft() == -1:
                        self.__Tree[self.__FirstNode].SetLeft(NewNode)
                    else:
                        self.__FirstNode = self.__Tree[self.__FirstNode].GetLeft()
                else:
                    if self.__Tree[self.__FirstNode].GetRight() == -1:
                        self.__Tree[self.__FirstNode].SetRight(NewNode)
                    else:
                        self.__FirstNode = self.__Tree[self.__FirstNode].GetRight()

# 1 b iii
    def OutputTree(self):
        for i in range(self.__NumberNodes):
            if self.__Tree[i].GetData() != "":
                print(self.__Tree[i].GetLeft(), self.__Tree[i].GetData(), self.__Tree[i].GetRight())
            else:
                print("No Nodes")
        

# 1 c i
TheTree = TreeClass()   