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
        
    else: #else by array indexing method, an array will be initialized with the length of maksimal character code - minimal character code. This way, the array size necessary for the operation will be reduced. Still the worst case scenario, the array will have 256 x 1 shape. After that a mathematical operation will be performed to store a value in index array respective to character ASCII code, aka simple hashing.
    
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
        
        #some adjusment are needed, since the maks value will be stored in the same index value, thus the upperbound will be increased by one before initializing an array
        maks, mins = ord(maks) + 1, ord(mins)
        array = [None] * (maks - mins)
        
        for char in string:
            ix = (ord(char) - mins) % maks
            if array[ix] is None:
                array[ix] = True
            else:
                return None
                
        return string

def main():
    return (is_unique(input()))

if __name__ == "__main__":
    main()
