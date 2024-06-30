#conver a decimal to ahexas string
def decimalToHex(decimalValue) :
    hex = " "
    
    while decimalValue != 0 :
        hexValue = decimalValue % 16
        hex = toHexChar(hexValue) + hex
        decimalValue = decimalValue // 16
    return hex

# convert an integer to a single hex digit as a charecter
def toHexChar(hexValue) :
    if 0 <= hexValue <= 9 :
        return char(hexValue + ord("0"))