def string_compression(string):
	#to perform string compression, first need to count for the similar character that lined up
    counter = 0
	
	#initiate dummy array with empty string as its value
    dummy = [""] * len(string)
    iy = 0
	
	#count character that are similar in line and compress it right away after different character is found.
    for ix in range(len(string) - 1):
        counter += 1
		
		#if character are different from the next one, then compress it
        if string[ix] != string [ix + 1]:
		
			#if there are 2 or more character then it's worth the compress else keep it without compress the character. i.e. aa -> a2; bbb -> b3; c -> c not c1
            dummy[iy] = string[ix] if counter == 1 else "".join([string[ix], str(counter)])
            iy += 1
			
			#reset the counter	
            counter = 0
    
	#compress the last character
    dummy[iy] = string[ix + 1] if counter == 0 else "".join([string[ix + 1], str(counter + 1)])
	
	#joining the string array into a single string. It's faster than adding the string during the loop process (i.e. string1 + string2), because adding string is like appending array.
    dummy = "".join(dummy)
	
	#is the compressed string length are the same or even longer, then return the initial string, else return the compressed one. 
    return string if len(dummy) >= len(string) else dummy
    
def main():
    return string_compression(input())
    
if __name__ == "__main__":
    main()
