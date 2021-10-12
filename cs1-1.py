#Author: JTI 10/12/21

x1 = input("Enter first x cordinate:")
y1 = input("Enter first y cordinate: ")
x2 = input("Enter second x cordinaye: ")
y2 = input("Enter second y cordinaye: ")

distance = (((int(x2) - int(x1)) ** 2) + ((int(y2) - int(y1)) ** 2) ** 1/2)
print(distance)