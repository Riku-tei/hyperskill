def sign(sign):
    if sign.startswith('+'):
        return '+'
    elif sign.startswith('-'):
        if len(sign) % 2 == 0:
            return '+'
        else:
            return '-'


def sign_num(sign, num):
    if sign == '+':
        return int(num)
    else:
        return int(num * (-1))


def help_info():
    print('The program calculates the sum or the substraction of numbers')


def parse():
    num_list = []
    num_array = inputs.split()
    # if num_array[0].startswith('+') or num_array[0].startswith('-'):
    #     num_array = sign(num_array[0])
    #     lens = len(num_array)
    #     for i in range(0, lens, 2):
    #         num_array[i] = sign(num_array[i])
    #         num_list.append(sign_num(num_array[i], int(num_array[i + 1])))
    #     print(sum(num_list))
    # else:
    num_list.append(int(num_array[0]))
    lens = len(num_array)
    for i in range(1, lens, 2):
        num_array[i] = sign(num_array[i])
        num_list.append(sign_num(num_array[i], int(num_array[i + 1])))
    print(sum(num_list))


while True:
    inputs = input()
    if inputs:
        if inputs == '/help':
            help_info()
        elif inputs == '/exit':
            print('Bye!')
            break
        else:
            parse()


