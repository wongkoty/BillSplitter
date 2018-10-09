def main():
    total = input('Enter Bill Total: ')
    get_total(total)
    people = input('How many people?: ')
    get_people(people)
    total = float(total)
    people = float(people)
    total = add_tax(total)
    split = total/people
    print('Each person pays ' + str(split) + ' dollars')

    import sys
    sys.exit(0)

def check_greater_than_zero(x):
    if float(x) <= 0:
        print('Bill should be greater than 0')
    else:
        return True

def get_people(people):

    while not check_number(people):
        return main()
        
    while not check_greater_than_zero(people):
        return main()
        
            
    return float(people)

def get_total(total):

    while not check_number(total):
        return main()
        
    while not check_greater_than_zero(total):
        return main()
        
            
    return float(total)
    

        
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

    location = input('What state are you in?: ')


    state = ['Wyoming','Wisconsin','West Virginia','Washington','Virginia','Vermont','Utah', 'Texas','Tennessee','South Dakota','South Carolina','Rhode Island','Puerto Rico' ,'Pennsylvania','Oregon','Oklahoma','Ohio','North Dakota','North Carolina','New York','New Mexico','New Jersey','New Hampshire','Nevada','Nebraska','Montana','Missouri','Mississippi','Minnesota','Michigan','Massachusetts','Maryland','Maine','Louisiana','Kentucky','Kansas','Iowa','Indiana','Illinois','Idaho','Hawaii','Guam','Georgia','Florida','District of Columbia','Delaware','Connecticut','Colorado','California','Arkansas','Arizona','Alaska','Alabama'];

    tax = ['0.06','0.0675','0.07','0.104','0.06','0.07','0.0835','0.0825','0.0975','0.06','0.09','0.07','0.115','0.08','0','0.11','0.08','0.08','0.075','0.08875','0.08688','0.12875','0','0.0825','0.075','0','0.1085','0.0725','0.07875','0.06','0.0625','0.06','0.055','0.12','0.06','0.1015','0.07','0.07','0.1025','0.085','0.04712','0.04','0.08','0.075','0.0575','0','0.0635','0.1','0.1025','0.11625','0.10725','0.07','0.135'];

    tax_from_state = dict(zip(state,tax))

    try:
        tax_from_state[location]

    except KeyError:
        print('Not a valid state')
        return add_tax(value)

    tax_adj_total = value * (float(tax_from_state[location])+1)

    return float(tax_adj_total)
    

