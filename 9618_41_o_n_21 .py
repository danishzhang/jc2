# 2a
class Picture:
    def __init__(self, Description, Width, Height, FrameColour):
        self.__Description = Description
        self.__Width = Width
        self.__Height = Height
        self.__FrameColour = FrameColour
    
# 2b
    def GetDescription(self):
        return self.__Description
    def GetHeight(self):
        return self.__Height
    def GetWidth(self):
        return self.__Width
    def GetColour(self):
        return self.__FrameColour
    
# 2c
    def SetDecription(self, description):
        self.__Description = description
    
# 2d
myArr = [Picture("",0,0,"") for i in range(100)]

# 2e
def ReadData():
    index = 0
    file = open('Pictures.txt','r' )
    tempdesc = file.readline().strip()
    while tempdesc != "":
        tempheight = file.readline().strip()
        tempwidth = file.readline().strip()
        tempcolour = file.readline().strip()
        myArr[index] = Picture(tempdesc, tempheight, tempwidth, tempcolour)
        index = index + 1
        tempdesc = file.readline().strip()

