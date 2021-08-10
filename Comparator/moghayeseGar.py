def compare(string1, string2):
    while True:
        if string1[0] < string2[0]:
            string1 = string1[1:]
        elif string1[0] > string2[0]:
            string2 = string2[1:]
        else:
            string1 = string1[1:]
            string2 = string2[1:]
            
        if not string1 and not string2:
            return 'Both strings are empty!'
        elif not string1:
            return string2
        elif not string2:
            return string1
        
        string1 = string1[::-1]
        string2 = string2[::-1]
        
