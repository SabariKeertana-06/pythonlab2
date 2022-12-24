#Circulating n values
s = int(input("Enter no of values in the list :"))
x = int(input("Enter no of times the value to be circulated :"))
list = []
for i in range (0,s):
    element = int(input("Enter value of the element :"))
    list.append(element)
print("Circulating The List")
for i in range(0,x):
    element_deleted=list.pop(0)
    list.append(element_deleted)
    print("The Circulated List after",i+1,"rotation",list)
