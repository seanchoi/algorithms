def tempConvert(degree, to):
    temp = 0
    if to == "F":
        temp = (9/5*degree)+32
    elif to == "C":
        temp = (degree-32)*5/9
    return temp

print(tempConvert(90, "F"))
print(tempConvert(194, "C"))
