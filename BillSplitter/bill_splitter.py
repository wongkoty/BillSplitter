def main():
    total = input('Enter Bill Total: ')
    get_total(total)
    people = input('How many people?: ')
    get_people(people)
    total = float(total)
    people = float(people)
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

main()
