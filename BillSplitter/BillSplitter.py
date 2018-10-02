total = float(input("Enter Bill Total: "))
people = int(input("Enter Number of people: "))
cash_credit = input('Cash or Credit?: ')
total_tax_adj = total * 1.08875
tips = total * 0.2
split = total_tax_adj/people
if str(cash_credit) == 'credit' or 'Credit':      
        min = input('Credit Card Minimum?: ')
        if int(split) < int(min):
                print("Not enough for credit")
        else:
                print('Each person pays ' + str(split) + ' dollars' 'and tips ' + str(tips))
        
else:
        print('Each person pays ' + str(split) + ' dollars' 'and tips ' + str(tips))
