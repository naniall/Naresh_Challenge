import itertools

valid = "Valid"
notValid= "Not Valid"
cardNumber = input("Enter your card number ")

def checkCard(cardNumber):
    cardNumber=str(cardNumber)
    if (len(cardNumber.split('-')) == 1 and len(cardNumber) == 16) or (len(cardNumber.split('-')) == 4 and all(len(i) == 4 for i in cardNumber.split("-"))):
        cardNumber = cardNumber.replace("-", "")
        try:
            int(cardNumber)
            if max(len(list(g)) for _, g in itertools.groupby(cardNumber)) > 3:
                result=notValid
            else:
                result = valid
        except ValueError as e:
            result = notValid
    else:
        result = notValid
    return result
print(checkCard(cardNumber))



