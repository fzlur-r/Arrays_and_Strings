def check_permutation(string1, string2):
    #get the length of the first string
	length = len(string1)
    
    #if the first and the seconde string not in the same length, it means those string are not a permutation
	if length != len(string2):
        return False
    
    #initialize the first-16 prime number
	prime_array = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    
	#initialize array to count character in a string
	char_array = [1] * 16
    
	#the first loop multiply the char_array, respective to the divisor value of char ascii code, with the prime number respective to the residual value of char ascii code.
	for char in string1:
        ix = ord(char)
        char_array[ix // 16] *= prime_array[ix % 16]
    
	#the second loop divide the char_array, respective to the divisor value of char ascii code, with the prime number respective to the residual value ov char ascii code.
    for char in string2:
        ix = ord(char)
        
		#if the array still can be divided with the prime number then it's still save to continue the loop
		if (char_array[ix // 16] % prime_array[ix % 16]) == 0:
            char_array[ix // 16] /= prime_array[ix % 16]
        
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
