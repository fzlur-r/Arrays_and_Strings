def is_unique(string):
    #this function is to determine if a string has all unique characters or not
    #if the string is unique then this function will return that string, else it will return None
	#the input argument is string
    #restriction: using only array and string data type
	
	#store the string's length, and then performing symtax based on it
    length = len(string)
	
    if length == 0: #if the string has no character then it's simply return None value
        return None
		
    elif length == 1: #if the string has one character then the string always unique thus will return string value
        return string
		
    elif length == 2: #if the string has two character then it's easier to just compare those character without looping.
        return string if string[0] != string[1] else None
		
    elif len(string) > 256: #if the string has more than 265 character, which the maksimal possible character in extended ASCII code, then it will always have at least one double character thus will return None
        return None
		
    else: #else by brute force method, an itteration will be conduct then comparing every character in string, and if there any similar character, None value will ber returned and the loop will stop 
        for count, char in enumerate(string[:-1]):
            for char2 in string[count+1:]:
                if char == char2:
                    return None
                
        return string #if the loop finish, then it means the string is unique.
