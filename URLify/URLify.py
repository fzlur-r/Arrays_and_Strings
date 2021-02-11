def URLify (string, true_length = None):
	#if true length of string are not given, then the true length will be the length of string without the space in the end of string
    if true_length is None or true_length > len(string):
        true_length = 0
        counter = 0
		
		#counting the space between the string and also the true length of string. It's easier to perform looping from last character to the beginning.
        for ix in range(len(string) - 1, -1, -1):
            if string[ix] != ' ' and true_length == 0:
                true_length = ix + 1
            elif string[ix] == ' ' and true_length != 0:
                counter +=2
    
	#else count the space between the string in range of true length     
    else:
        counter = 0
		
		#counting the space character
        for ix in range(true_length):
            if string[ix] == ' ':
                counter += 2
    
	#while it's easier to just append value to array in python, but the time cost will be great, since appending value is just looping the whole array and add the value into the last index. Thus initialize array with desired length and assign value to array index will be faster.
    dummy = [''] * (true_length + counter)
    counter = 0
	
	#performing loop based on true length to find the space character in string and convert it to "%20"
    for ix in range(true_length):
		#if the character is space, then it will be converted
        if string[ix] == ' ':
            dummy[ix + counter] = '%'
            dummy[ix + counter + 1] = '2'
            dummy[ix + counter + 2] = '0'
			
			#counter used to keeping the track of shifted index
            counter += 2
			
		#else, keep the character as it is
        else:
            dummy[ix + counter] = string[ix]
            
    return "".join(dummy)
    
def main():
    return URLify(input())
    
if __name__ == "__main__":
    main()
