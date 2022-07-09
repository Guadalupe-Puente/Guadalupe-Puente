#2.3.1.18 Tu propio split
#Guadalupe Puente
def mysplit(strng):
    #
    # put your code here
    #
    result = []
    words = ''
    for char in strng:
        if char != ' ':
            words += char
        else:
            if words:
                result.append(words)
            words = ''
            
            
    result.append(words)
    
    for item in result:
        if item == '':
            result.remove(item)
    
    return result

print(mysplit("Ser o no ser, esa es la pregunta"))
print(mysplit("Ser o no ser,esa es la pregunta"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))