#1a
BeverageQueue = [None for i in range(10)]
BeverageFrontPointer = 0
BeverageRearPointer = 0


#1bi
def DisplayMenu():
    global menu
    file = open('BeverageData.txt', 'r')
    menu = file.readline().strip()
    file.close()

#1bii (recheck cuz 6 marks)
def TakeOrder():
    order = input("Choose one or more beverages: ")
    if order == menu:
        fileOrder = open('Order.txt', 'w')
        fileOrder.writelines()
    

#1b iii
def EnqueueBeverage(DataToEnqueue):
    global BeverageRearPointer
    global BeverageFrontPointer
    if BeverageRearPointer == 10:
        return False
    else:
        BeverageQueue[BeverageRearPointer] = DataToEnqueue
        BeverageRearPointer = BeverageRearPointer + 1
        return True

#1b iv
def ReadOrderData():
    data = open('Order.txt', 'r')
    orderData = data.readline().strip()
    EnqueueBeverage(orderData)

#1c i
def DequeueBeverage():
    global BeverageRearPointer
    global BeverageFrontPointer
    if BeverageFrontPointer == BeverageRearPointer:
        return ""
    else:
        ReturnData = BeverageQueue[BeverageFrontPointer]
        BeverageFrontPointer = BeverageFrontPointer + 1
        return ReturnData
    
#1 c ii
def ServeItem():
    global BeverageRearPointer
    global BeverageFrontPointer
    if BeverageRearPointer != len(BeverageQueue) -1:
        orderDequeue = DequeueBeverage()
        print("You ordered ", orderDequeue)
    else:
        if BeverageRearPointer == BeverageFrontPointer:
            print("No more orders to serve")
#1d i

DisplayMenu()
TakeOrder()
ReadOrderData()
ServeItem()

#1d ii