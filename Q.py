class Q :
    def __init__(self):
        self.arr=[]

    def enque (self, data):
        self.arr.append(data)

    def deque (self):
        if len(self.arr)>0 :
            self.arr.pop(0)
        else:
            print("Dear Q is empty !!")

    def display(self):
        if len(self.arr)>0 :
            for i in range (len(self.arr)):
                print(f"item {i} = {self.arr[i]}")
        else:
            print("Dear Q is empty !!")

q =Q()
while True :
    print("\n\n")
    print ("choose operation to do : ")
    print ("1. enque")
    print ("2. deque")
    print ("3. display")
    c = int (input ("your choise : "))

    match c :
        case 1:
            d = int (input ("your data : "))
            q.enque( d )

        case 2:
            q.deque()
            print("Done !!")

        case 3:
            q.display()

        case _ :
            print ("Quit")
            break











