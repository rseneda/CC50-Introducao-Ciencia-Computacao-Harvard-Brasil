#AMERICAN 15 DIGITOS, INICIO 34 OU 37 - 348282246310005 - 378282246310005
#VISA 13 OU 16 DIGITOS, INICIO 4 - 4312888888881881 
#MASTER 16 DIGITOS, INICIO 51, 52, 53, 54 OU 55 - 5405105105105100 

from cs50 import get_string
def main():
    
    number = get_string("Número do cartão: ")

    res = [int(x) for x in str(number)]

    if res[0] == 3 and (res[1] == 7 or res[1] == 4):
        print("AMEX")
    elif res[0] == 5 and (res[1] == 1 or res[1] == 2 or res[1] == 3 or res[1] == 4 or res[1] == 5):
        print("MASTERCARD")
    elif res[0] == 4:
       print("VISA")
    else:
        print("INVÁLIDO")
        return 1

    formula1 = []
    formula2 = []

    while (len(res) != 0):
        last = res.pop()
        formula2.append(last)
        if len(res) == 0:
            break
        second_last = res.pop()
        formula1.append(second_last)

    result = 0

    for item in formula1:
        if (item * 2) < 10:
            result += item * 2
        else:
            new = (item * 2) % 10
            result += new
            new = (item * 2)//10
            result += new

    for item in formula2:
        result += item

main()
