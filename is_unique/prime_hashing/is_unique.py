def is_unique(string):
    #this function is to determine if a string has all unique characters or not
    #if the string is unique then this function will return that string, else it will return None
    #the input argument is string
    #restriction: using only array and string data type
    
    #if the string is unique then this function will return that string, else it will return None
    length = len(string)
    
    if length == 0: #if the string has no character then it's simply return None value
        return None
        
    elif length == 1: #if the string has one character then the string always unique thus will return string value
        return string
        
    elif length == 2: #if the string has two character then it's easier to just compare those character without looping.
        return string if string[0] != string[1] else None
        
    elif length > 256: #if the string has more than 265 character, which the maksimal possible character in extended ASCII code, then it will always have at least one double character thus will return None
        return None
        
    else: #else by prime hashing method, an array will be initialized with the shape of 7 x 1. This way, the array size are in constant value. After that a mathematical operation to find the first - 40 prime number respective to character divisor value which stored in array index respective to character residual value. If the character already exist, then the value stored in array can be divided by the prime number which will return None, else the loop is continue and finally return the unique string.
    
        #this loop will find the minimum character in a string
        mins = string[0]
        for char in string[1:]:
            if mins > char:
                mins = char
         
        #this loop will find the maksimum character in a string   
        maks = string[0]
        for char in string[1:]:
            if maks < char:
                maks = char
    
        #in pythonic ways, the upper syntax can be substitute by max() and min() method which return the maximum and minimum value in array
        #mins, maks = ord(min(string)), ord(max(string))
        
        mins, maks = ord(mins), ord(maks)
        array = [None]*7
        
        for char in string:
            value = ord(char) - mins
            ix = value % 7
            n = (value // 7) + 1
            prime = n * (n - 1) + 41
            
            if array[ix] is None:
                array[ix] = prime
            elif array[ix] % prime == 0:
                return None
            else:
                array[ix] *= prime

        return string
