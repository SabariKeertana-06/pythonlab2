#Calculating bill for 5 books
bk1 = float(input("Enter cost of book1 :"))
bk2= float(input("Enter cost of book2 :"))
bk3 = float(input("Enter cost of book3 :"))
bk4 = float(input("Enter cost of book4 :"))
bk5 = float(input("Enter cost of book5 :"))
total = bk1+bk2+bk3+bk4+bk5
discount = total - (5/100)
print("The Total Cost of Books :",total)
print("Total Cost after Discount :",discount)
print("THANKS FOR SHOPPING !! :) ")
