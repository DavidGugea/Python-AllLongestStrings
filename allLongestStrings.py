def allLongestStrings(inputArray):
    ar = [] 
    for element in inputArray:
        c = list(element) 
        ar.append(c)
    
    BIGGEST_LEN = len(ar[0])
    b = []
    for list_element in inputArray:
        c = len(list_element)
        if c > BIGGEST_LEN:
            BIGGEST_LEN = c 
    
    for element in inputArray:
        if len(element) == BIGGEST_LEN:
            b.append(element)
    
    return b
            
