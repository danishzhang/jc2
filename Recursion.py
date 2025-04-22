# Sum of array
# array = [1,2,3,4,5,6,7,8,9,10]
# def sum_of_array(array):
#         if len(array) == 1 :
#             return array[0]
#         else:
#             return array[0] + sum_of_array(array[1:])
            
# print(sum_of_array(array))

# Reverse string
string = "abcde"
def reverse_str(string):
     if len(string) == "":
          return string
     else:
          return  reverse_str(string[1:]) + string[0]
     
print(reverse_str(string))
