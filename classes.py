numClasses = int(input('Enter the number of hours of classes given in the month: '))
pHours = int(input('Inform the value of the lesson hour: '))
pDiscount = int(input('Inform the tax discount percentage: '))
sGross = int
sLiquid = int

sGross = pHours * numClasses
sLiquid = sGross - (sGross * pDiscount) / 100

print('The value of the gross salary is: ', sGross)
print('The value of the net salary is: ', sLiquid)