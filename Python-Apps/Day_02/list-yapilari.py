my_list = ["hello", 5.6, 137, True, 25, "son"] 

# print(my_list[-1]) 

# List yapsında birden fazla eleman getirme :

# Slicing ; parçalara ayırma  
# Slicing syntax :   my_list[start:stop:step]  
# stop değeri dahil edilmez.
# step değeri default (varsayılan ) : 1
# start, stop ve step değerini girmeyebilirsiniz. [:]
# hiçbir değer girmediğinizde start için ilk index değerini alır, stop için son indexi alır, step için de 1 alır.

print(my_list[:]) 

print(my_list[1:]) 

print(my_list[::2]) 

print(my_list[::-1])    # Bu kullanım bir listi tersten yazdırır.

print(my_list[-1:-5:-2])


x= int(input("enter a nummer!"))

y=x*x-12*x+11

print(y)

days=['PAZARTESI','SALI', 'CARSAMBA', 'PERSEMBE','CUMA', 'CUMARTESI','PAZAR']

x=int(input("enter a nummer between 1 and 7!"))
print(days[x-1])



