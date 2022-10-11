price = 50
if price < 100:
    print("price is less than 100")

quantity = 5
if price*quantity < 500:
    print("price*quantity is less than 500") #indentation
    print("price= ",price)
    print("quantity= ", quantity)
if price*quantity < 100:
     print("price is less than 500")
     print("price= ", price)
     print("quantity= ", quantity)
print('no if block executed.')#out of block statement

price = 100
if price > 100:
    print("price is greater than 100")
if price == 100:
    print("price is 100")
if price < 100:
    print("price is less than 100")

#else condition
price = 50
if price >= 100:
    print("price is greater than 100")
else:
    print("price is less than 100")

#if-elif condition
price = 100
if price > 100:
    print("price is greater than 100")
elif price ==100:
    print("price is 100")
elif price <100:
    print("price is less than 100")

#if-elif-else conditions
price = 50
if price > 100:
    print("price is greater than 100")
elif price ==100:
    print("price is 100")
else:
    print("price is less than 100")

#####
price = 50
quantity = 5
amount = price * quantity
if amount > 100:
    if amount > 500:    #dented if statement i.e a multidimensional statement more lie an if in an if
        print("amount is greater than 500")
    else:
        if amount < 500 and amount > 400:
            print("amount is")
        elif amount < 500 and amount > 300:
            print("amount is between 300 and 500")
        else:
            print("amount is between 200 and 500")
elif amount == 400:
    print('amount is 100')
else:
    print ('amount is less than 100')

