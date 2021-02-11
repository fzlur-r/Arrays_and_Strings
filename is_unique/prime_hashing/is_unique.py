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
        
    else: #else by prime hashing method, an array will be initialized with the shape of 16. This way, the array size are in constant value. After that a prime number of the first - 16 is called respective to the character residual value. Then if the character is already exist, then the value stored in array can be divided by the prime number which will return None, else the prime number multiplied with the value in array index respective to character divisor value and the loop is continue and finally return the unique string.
    
        prime_array = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
        array = [1] * 16
        
        for char in string:
            value = ord(char)
            if array[value // 16] % prime_array[value % 16] == 0:
                return None
            else:
                array[value // 16] *= prime_array[value % 16]

        return string

def main():
    return is_unique(input())

if __name__ == "__main__":
    main()
