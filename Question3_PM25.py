#1 a i
class Device:
    def __init__(self, device_name, brand, battery_life, price):
        self.__device_name = device_name
        self.__brand = brand
        self.__battery_life = battery_life
        self.__price = price

    def get_device_name(self):
        return self.__device_name
    
    def get_brand(self):
        return self.__brand
    
    def get_battery_life(self):
        return self.__battery_life

    def get_price(self):
        return self.__price
    
    def print_details():
        print("The decive name is ", Device.get_device_name()," from", Device.get_brand()," and has a battery life of ", Device.get_battery_life(), 
              " with the price of ", Device.get_price())
        
#1 a ii
class Phone():
    def __init__(self, storage):
        self.__storage = storage
    
    def get_storage(self):
        return self.__storage
    
    def print_details():
        print("The decive name is ",Device.get_device_name()," from ",Device.get_brand()," with a battery life of ",Device.get_battery_life(), 
              " and a storage of ",Phone.get_storage(), " with the price of ",Device.get_price())
        
#1 a iii
class Laptop:
    def __init__(self, ram):
        self.__ram = ram

    def get_ram(self):
        return self.__ram
    
    def print_details():
        print("The decive name is ",Device.get_device_name()," from ",Device.get_brand()," with a battery life of ",Device.get_battery_life(), 
              " and a RAM of ",Laptop.get_ram(), " with the price of ",Device.get_price())



class Tablet:
    def __init__(self, screen_size):
        self.__screen_size = screen_size

    def get_screen_size(self):
        self.__screen_size

    def print_details():
         print("The decive name is ",Device.get_device_name()," from ",Device.get_brand()," with a battery life of ",Device.get_battery_life(), 
              " and a screen size of ",Tablet.get_screen_size(), " with the price of ",Device.get_price())

#2 b
def ReadDeviceData():
    myArr = [Device("","",-0,0) for i in range()]