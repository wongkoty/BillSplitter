total = float(input("Enter Bill Total: "))
people = int(input("Enter Number of people: "))
cash_credit = input('Cash or Credit?: ')
total_tax_adj = total * 1.08875
tips_person = (total * 0.2)/people
split = total_tax_adj/people
if str(cash_credit) == 'credit':      
        min = input('Credit Card Minimum?: ')
        if int(split) < int(min):
                print("Not enough for credit")
        else:
                print('Each person pays ' + str(round(split, 2)) + ' dollars' ' and tips ' + str(round(tips_person, 2)))
        
else:
        print('Each person pays ' + str(round(split, 2)) + ' dollars' ' and tips ' + str(round(tips_person, 2)))
