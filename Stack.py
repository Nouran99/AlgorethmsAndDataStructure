class Node :
    def __init__(self, data):
        self.next = None
        self.data = data

class stack :
    def __init__(self):
        self.head= self.tail = None

    def push (self , data) :
        n = Node(data)
        if (self.head == None):
            self.head= self.tail= n
        else :
            self.tail.next = n
            self.tail = n

    def pop (self):
        if (self.head == None) :
            print("Dear, Stack is empty !!")
        else:
            if (self.head == self.tail):
                self.tail= None
            else:
                new_n = self.head
                while (new_n.next.next != None ):
                    new_n= new_n.next
                new_n.next = None
                self.tail = new_n
        return new_n

    def isempty (self):
        if (self.head == None) :
            print("Dear, Stack is empty !!")
        else:
            print("Dear, Don't worry Stack full !!")

    def display(self):
        if (self.head != None) :
            new_n = self.head
            while (new_n != None):
                print( new_n.data )
                new_n = new_n.next
        else:
            print("Dear, Stack is empty !!")


my_stack = stack()
while True :
    print("\n\n")
    print ("choose operation to do : ")
    print ("1. push")
    print ("2. pop")
    print ("3. display")
    print ("4. check if it is empty")
    c = int (input ("your choise : "))

    match c :
        case 1:
            data = int (input ("your data : "))
            my_stack.push(data)

        case 2:
            my_stack.pop()
            print("Done !!")

        case 3:
            my_stack.display()

        case 4:
            my_stack.isempty()

        case _ :
            print ("Quit")
            break










