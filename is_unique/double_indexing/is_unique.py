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
		
    elif length == 2: #if the string has two character then it's easier to just compare those character without looping
        return string if string[0] != string[1] else None
		
    elif length > 256: #if the string has more than 265 character, which the maksimal possible character in extended ASCII code, then it will always have at least one double character thus will return None
        return None
		
    else: #else by array double indexing method, an array will be initialized with the shape of length x 1. If there's two or more difference character landing on the same index, then the second array will be initialized with the size of (max - min) // length + 1 and all these character would then replaced to this new array. Finnaly like before, if there are similar character, the function will return None value and the loop will stopped.

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
        array = [None]*length
		
        for char in string:
            value = ord(char) - mins
            ix = value % length
            iy = value // length
            if array[ix] is None:
                array[ix] = iy
            elif type(array[ix]) is list:
                if array[ix][iy] is None:
                    array[ix][iy] = iy
                else:
                    return None
            elif array[ix] == iy:
                return None
            else:
                foo = array[ix]
                array[ix] = [None] * (((maks - mins) // length) + 1)
                array[ix][foo] = foo
                array[ix][iy] = iy
				
        return string
	
def main():
    return (is_unique(input()))

if __name__ == "__main__":
    main()
