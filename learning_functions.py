list = [1, 3, -60, 999, 0,]

def findMax(list):
    highest = list[0]
    for value in list:
        if value > highest:
            highest = value
    return(highest)