def main():
    total = get_total()
    people = int(input("Enter Number of people: "))
    split = total/people
    print('Each person pays ' + str(split) + ' dollars')

def check_greater_than_zero(total):
    if total <= 0:
        print('Invalid number my guy')
    else:
        return True


def get_total():

    total = input('Enter Bill Total: ')

    while not check_number(total):
        get_total()
             
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
