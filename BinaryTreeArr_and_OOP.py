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
    def InsertionNode(self, NewNode):
        if self.__NumberNodes == 0:
            self.__Tree[self.__NumberNodes] = NewNode
            self.__NumberNodes =+ 1
            self.__FirstNode = 0
        else:
            self.__Tree[self.__NumberNodes] = NewNode
            
            while True:
                if self.__Tree[self.__FirstNode].GetData() > NewNode.GetData():
                    self.__Tree[self.__FirstNode].GetLeft() 


