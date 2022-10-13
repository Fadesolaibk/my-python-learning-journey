cost_price = int(input('Please enter cost price: '))

if cost_price > 100000:
    task = (15/100)*cost_price
    print ('cost price:',cost_price, ',task is 15%:',task)
elif cost_price >50000 and score <= 100000:
    task = (10/100)*cost_price
    print ('cost price:',cost_price, ',task is 10%:',task)

else:
    task = (5/100)*cost_price
    print ('cost price:',cost_price, ',task is 5%:',task)


