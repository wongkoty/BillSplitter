TAXES_BY_STATE = {
    'Alabama' : '0.135',
    'Alaska': '0.070',
    'Arizona': '0.107',
    'Arkansas': '0.116',
    'california' : '0.103',
    'colorado' :  '0.100',
    'connecticut': '0.064',
    'delaware':  '0.000',
    'district of columbia': '0.058',
    'florida': '0.075',
    'georgia': '0.080',
    'guam':  '0.040',
    'hawaii': '0.047',
    'idaho':  '0.085',
    'illinois': '0.103',
    'indiana': '0.070',
    'iowa':  '0.070',
    'kansas': '0.102',
    'kentucky': '0.060',
    'louisiana': '0.120',
    'maine': '0.055',
    'maryland':  '0.060',
    'massachusetts': '0.063',
    'michigan': '0.060',
    'minnesota':  '0.079',
    'mississippi': '0.073',
    'missouri':  '0.109',
    'montana': '0.000',
    'nebraska':  '0.075',
    'nevada': '0.083',
    'new hampshire': '0.000',
    'new jersey': '0.129',
    'new mexico':  '0.087',
    'new york':  '0.089',
    'north carolina': '0.075',
    'north dakota': '0.080',
    'ohio': '0.080',
    'oklahoma': '0.110',
    'oregon':  '0.000',
    'pennsylvania':  '0.080',
    'puerto rico': '0.115',
    'rhode island':  '0.070',
    'south carolina':  '0.090',
    'south dakota':  '0.060',
    'tennessee':  '0.098',
    'texas':  '0.083',
    'utah': '0.084',
    'vermont': '0.070',
    'virginia':  '0.060',
    'washington':  '0.104',
    'west virginia': '0.070',
    'wisconsin': '0.068',
    'wyoming': '0.060',
}

def main():
    total = get_bill_total()
    people = input('How many people?: ')
    get_people(people)
    total = float(total)
    people = float(people)
    total = add_tax(total)
    total = add_tip(total)
    split = total/people
    split_credit_min = check_credit_min(split)
    print('Each person pays ' + str(split_credit_min) + ' dollars')

def get_bill_total():
    total = 0
    while True:
        total = input('Enter Bill Total: ')
        try:
            total = float(value)
            if total <= 0:
                print('Bill should be greater than 0')
            else:
                break
        except ValueError:
            print('"{}" is not a number\n'.format(value))
            print('Please put a valid number\n')
    return total


def check_greater_than_zero(x):
    if float(x) <= 0:
        return False
    else:
        return True

def get_total(total):

    while not check_number(total):
        return main()

    while not check_greater_than_zero(total):
        return main()
    return float(total)

def get_people(people):

    while not check_number(people):
        return main()

    while not check_greater_than_zero(people):
        return main()

    return float(people)



def check_number(value):
    try:
        total = float(value)
        return True;
    except ValueError:
        print('"{}" is not a number'.format(value))
        print('Please put a valid number\n')
        return False


def meow():
    return 'meow'


def add_tax(value):
    tax = 0.0
    while True:
        location = input('What state are you in?: ')
        valid_states = {state.lower(): state for state in TAXES_BY_STATE.keys()}
        if location.lower() not in valid_states:
            print('Not a valid state')
        else:
            tax = TAXES_BY_STATE[valid_states[location.lower]]
            break
    return value * (float(tax)+1)

def add_tip(value):
    tip = input('What percent tip would you like to add?: ')
    try:
        float(tip)

    except ValueError:
        print('Not a valid tip amount')
        return add_tip(value)

    if float(tip) <= 0:
        print('Tip must be greater than zero')
        return add_tip(value)

    total_tip = ((float(tip)/100) + 1) * value

    return float(total_tip)

def check_credit_min(value):
    credit_check = input('Cash or Credit?: ').lower()

    if credit_check == 'credit':
        credit_min = input('What is the credit card minimum? If no minimum, type 0: ')
        if float(credit_min) > value:
            print('Not enough for credit')
            return check_credit_min(value)
        else:
            return(value)
    if credit_check == 'cash':
        return(value)
    else:
        print('Please enter cash or credit')
        return check_credit_min(value)

if __name__ == '__main__':
    main()
