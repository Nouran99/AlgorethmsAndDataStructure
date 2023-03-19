class item:
    def __init__(self , wight , value , name):
        self.wight = wight
        self.value = value
        self.v_over_w = value/wight
        self.name = name

    def __repr__(self):
        return f"\n name = {self.name} \n {self.wight} = wight, {self.value} = value, {self.v_over_w} = value/wight"


class knapsack :
    def __init__(self, lista,max_wight ):
        self.list =lista
        self.solution =[]
        self.max_wight =max_wight

    def arrange_lista (self):
        for i in range (0,len(self.list)):
            if self.list[i].wight > self.max_wight:
                self.list.pop (i)

    def sortbywight (self):
        self.arrange_lista()
        self.list =sorted(self.list ,key= lambda x : x.wight)
        curr_w =0
        for ii in range (0,len(self.list)):
            curr_w += self.list[ii].wight
            if curr_w <= self.max_wight :
                self.solution.append(self.list[ii])
            else:
                curr_w -= self.list[ii].wight
        r = self.max_wight - curr_w
        if r !=0 :
            new_persent = r / self.list[ii].wight
            print(f"we will use {new_persent} from {self.list[ii]}")
        return self.solution

    def sortbyvalue(self):
        self.arrange_lista()
        self.list = sorted(self.list, key=lambda x: x.value ,reverse= True)
        curr_w =0
        for ii in range (0,len(self.list)):
            curr_w += self.list[ii].wight
            if curr_w <= self.max_wight :
                self.solution.append(self.list[ii])
            else:
                curr_w -= self.list[ii].wight
            r = self.max_wight - curr_w
            if r != 0:
                new_persent = r / self.list[ii].wight
                print(f"we will use {new_persent} from {self.list[ii]}")
        return self.solution

    def sortbyvoverw(self):
        self.arrange_lista()
        self.list = sorted(self.list, key=lambda x: x.v_over_w , reverse= True)
        curr_w =0
        for ii in range (0,len(self.list)):
            curr_w += self.list[ii].wight
            if curr_w <= self.max_wight :
                self.solution.append(self.list[ii])
            else:
                curr_w -= self.list[ii].wight
            r = self.max_wight - curr_w
            if r != 0:
                new_persent = r / self.list[ii].wight
                print(f"we will use {new_persent} from {self.list[ii]}")
        return self.solution

    def sortbywight0 (self):
        self.arrange_lista()
        self.list =sorted(self.list ,key= lambda x : x.wight)
        curr_w =0
        for ii in range (0,len(self.list)):
            curr_w += self.list[ii].wight
            if curr_w <= self.max_wight :
                self.solution.append(self.list[ii])
            else:
                curr_w -= self.list[ii].wight
        return self.solution

    def sortbyvalue0(self):
        self.arrange_lista()
        self.list = sorted(self.list, key=lambda x: x.value ,reverse= True)
        curr_w =0
        for ii in range (0,len(self.list)):
            curr_w += self.list[ii].wight
            if curr_w <= self.max_wight :
                self.solution.append(self.list[ii])
            else:
                curr_w -= self.list[ii].wight

        return self.solution

    def sortbyvoverw0(self):
        self.arrange_lista()
        self.list = sorted(self.list, key=lambda x: x.v_over_w , reverse= True)
        curr_w =0
        for ii in range (0,len(self.list)):
            curr_w += self.list[ii].wight
            if curr_w <= self.max_wight :
                self.solution.append(self.list[ii])
            else:
                curr_w -= self.list[ii].wight

        return self.solution

item1= item (5,50,"i1")
item2= item (10,60,"i2")
item3= item (20,140,"i3")
dlista =[ item1 ,item2 ,item3]

while True :
    print("plz choose the way :")
    print("1- enter items properties manually")
    print("2- use default items")
    choice = int(input("your choice :  "))

    print("plz choose the problem :")
    print("1- Fractional")
    print("2- 0/1 (as Bonus)")
    choice2 = int(input("your choice :  "))


    match choice:
        case 2:
            print("use default items")
            print(dlista)
            maxi = int(input("your wight :  "))
            knapsack1 = knapsack(dlista, maxi)
            print("plz choose the way :")
            print("1- minimize wight")
            print("2- maximize value")
            print("3- maximize value over wight")
            choice3 = int(input("your choice :  "))

        case 1:
            print("inter items as :")
            maxi = int(input("your wight :  "))
            n = int(input("num of items :  "))
            lista = []
            for i in range(0, n):
                name = input(f"item {i} name:  ")
                wight = int(input(f"item {i} wight:  "))
                value = int(input(f"item {i} value:  "))
                lista.append(item(wight, value, name))
            knapsack1 = knapsack(lista, maxi)
            print("plz choose the way :")
            print("1- minimize wight")
            print("2- maximize value")
            print("3- maximize value over wight")
            choice3 = int(input("your choice :  "))

        case _:
            print("wrong choice")
            continue

    match choice2:
        case 1:
            match choice3:
                case 1:
                    print(knapsack1.sortbywight())
                case 2:
                    print(knapsack1.sortbyvalue())
                case 3:
                    print(knapsack1.sortbyvoverw())

        case 2:
            match choice3:
                case 1:
                    print(knapsack1.sortbywight0())
                case 2:
                    print(knapsack1.sortbyvalue0())
                case 3:
                    print(knapsack1.sortbyvoverw0())


        case _:
            print("wrong choice")
            continue

