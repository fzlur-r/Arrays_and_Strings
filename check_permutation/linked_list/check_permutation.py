#initialize node class. A node have value, and counter of how many its value exist. The node also have pointer next which will used to point to the next node.
class node:
    def __init__(self, value):
        self.value = value
        self.counter = 1
        self.next = None

#initialize linked list class. A linked list can add a value and also remove the value by substracting its counter.
class link:
    def __init__(self):
        self.body = None
    
    #adding value counter to a node
    def add_val(self, value):
        if self.body is None:
            self.body = node(value)
        
        elif self.body.value == value:
            self.body.counter += 1
        
        else:
            self.body.next = self.add_pointer(value, self.body.next)
    
    #adding value counter to the next node
    def add_pointer(self, value, nodes):
        if nodes is None:
            nodes = node(value)
        
        elif nodes.value == value:
            nodes.counter += 1
            
        else:
            nodes.next = self.add_pointer(value, nodes.next)
            
        return nodes
	
    #substracting value counter from a node
    def substract_val(self, value):
        if self.body is not None:
            if self.body.value == value and self.body.counter > 0:
                self.body.counter -= 1
        
            elif self.body.value == value and self.body.counter <= 0:
                self.body = None
        
            else:
                self.body.next = self.substract_pointer(value, self.body.next)
                if self.body.next is None:
                    self.body = None
    
    #substracting value counter from the next node
    def substract_pointer(self, value, nodes):
        if nodes is not None:
            if nodes.value == value and nodes.counter > 0:
                nodes.counter -= 1
            
            elif nodes.value == value and nodes.counter <= 0:
                nodes = None
                
            else:
                nodes.next = self.substract_pointer(value, nodes.next)
                if nodes.next is None:
                    nodes = None
        
        if nodes is None:
            return None
        else:
            return nodes
                
def check_permutation(string1, string2):
    #get the length of the first string
    length = len(string1)
    
    #if the first and the seconde string not in the same length, it means those string are not a permutation
    if length != len(string2):
        return False
    
    #else counting how many character present in each string
    else:
        linked_list = link()
		
        #first loop count the character
        for char in string1:
            linked_list.add_val(char)
        
        #second loop substract the counter of character
        for char in string2:
            linked_list.substract_val(char)
			
            #if the linked list has None value in its counter (which mean lower than 0) then those string are not a permutaion
            if linked_list.body is None:
                return False
				
        #if the loop have been succesfully, then those string are permutation of each other
        return True

def main():
    string1 = input()
    string2 = input()
    return check_permutation(string1, string2)
    
if __name__ == "__main__":
    main()
