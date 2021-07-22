def priceIncVatCalculate():
    totalPrice = int(input("Input the price : "))
    percVat = int(input("Input the %VAT : "))
    result = totalPrice + (totalPrice * percVat/100)
    return result

print(priceIncVatCalculate())
