# 2
# Output : (OrderNumber,Quantity*Price per Item)
# eg : ( 34587 , 4*40.95)

someOrders = [
    [34587,"Learning With Python, Mark Lutz",4,40.95],
    [98762,"Programming Python, Mark Lutz",5,56.8],
    [77226,"Head First Python, Paul Barry",3,32.95],
    [88112,"Einführung in Python3, Bernd Klein",3,24.99]]


getTotal = lambda order: (order[0], order[2]*order[3])

orderTotals = map(getTotal,someOrders)
myList = list(orderTotals)

# for order in myList:
#     print("Order number: %s\tTotal: %.2f" % (order[0],order[1]))

print(myList)