def check_permutation(string1, string2):
    #get the length of the first string
    length = len(string1)
    
    #if the first and the seconde string not in the same length, it means those string are not a permutation
    if length != len(string2):
        return False
    
    #else counting how many character present in each string
    else:
	#initialize array to store the character counter respective to its ascii code value
    	char_array = [0] * 256
    
    	#add the value counter to array
    	for char in string1:
        	char_array[ord(char)] += 1
    
    	#substract the value counter to array
    	for char in string2:
        	#if the counter still more than 0 before substracting the its still save to continue the loop
        	if char_array[ord(char)] > 0:
            	char_array[ord(char)] -= 1
        
        	#else the second string have more or new character which mean those string are not a permutation
        	else:
            	return False
    
    	#if the loop finish succesfully, then those string are permutation of each other
    	return True
    
def main():
    string1 = input()
    string2 = input()
    return check_permutation(string1, string2)
    
if __name__ == "__main__":
    main()
