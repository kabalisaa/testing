from beautifultable import BeautifulTable
from tabulate import tabulate

# My Custom Inclusive Range
class Irange:
    def __init__(self,*args):
        ars=args
        numargs=len(ars)
        
        if numargs<1: raise TypeError("Myst Have At lest one parameter")
        elif numargs==1:
            self.start=0
            self.end=ars[0]
            self.step=1
        elif numargs==2:
            (self.start,self.end)=ars
            self.step=1
        elif numargs==3:
            (self.start,self.end,self.step)=ars
        else: raise TypeError("Too Many Arguments ")
    
    def __iter__(self):
        i=self.start
        while i <= self.end:
            yield i
            i+=self.step

# Our Great class
class Store:
    # And this is how we do constructors in python 
    def __init__(self):
        self.stock={} #initializing the our constructor
      
        self.min=float(input("What's your Minimum: "))
        self.max=float(input("What's your Maximum: "))

        print(tabulate([["value"+str(i+1) for i in range(len(list(Irange(self.min,self.max,1.251))))]]))

        for i in Irange(self.min,self.max,1.25):
            self.stock[i]=input().split()
        
    
    def show_stock(self):
        print("")
        print("\t Marie's Stock")
        stockKeys=list(map(str, self.stock.keys()))
        table = BeautifulTable()
        [table.rows.append(self.stock.get(i)) for i in self.stock]
        table.columns.header=(stockKeys)
        table.rows.header=(stockKeys)
        print(table)
    def get_stock(self,cylinder,sphere):
        keys=self.stock.keys()
        idx=self.stock.get(cylinder)[list(keys).index(sphere)]
        return ("Stock Left for cylinder/Sphere {}/{} : {} glasses".format(cylinder,sphere,idx))
    
# Our Object
marie=Store()

# Show the stock
marie.show_stock()
