numbers = []
numbers_len = int(input("List length : "))

for x in range(numbers_len) :
     z = float(input("Enter Numbers : "))
     numbers.append(z)
     

def smallest_number():
     smallest_num = numbers[0]
     for smallest in numbers:
         if smallest < smallest_num :
             smallest_num = smallest

     print(smallest_num) 

smallest_number()             
