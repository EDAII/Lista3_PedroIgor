from random import randint
def numbers_gen():
    number_list = []
    while(len(number_list) < 105):
        n = int(randint(0, 10000)*randint(0, 100)/100)
        if not n in number_list:
            number_list.append(n)
    return number_list