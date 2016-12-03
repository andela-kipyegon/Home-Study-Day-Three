class BinarySearch(list):
    num_list = []
    
    def __init__(self,a,b):
         """constructor"""

        super(BinarySearch,self).__init__()
        self.length = a
        self.step = b
        for i in range(self.step,(self.length*self.step)+1,self.step):
           self.append(i)
        self.num_list = self
        
       
    def search(self,item):
        """search fxn to search an item"""

        first = 0
        last = len(self.num_list)-1
        found = False
        list_item = False
        count = 0
        
        #handles if item no in list
        try:
            index = self.index(item)
            list_item = True
        except ValueError:
            index = -1
            list_item = False

        #binary algorithm
        while first<=last and not found and list_item and item != self.num_list[last]:
              
            midpoint = (first + last)//2
            if self.num_list[midpoint] == item:
                index =midpoint
                count += 1
                found = True
            else:
              if item < self.num_list[midpoint]:
                  last = midpoint-1
                  count += 1
              else:
                  first = midpoint+1
                  count += 1
                    
        return {"count":count, "index":index}
       