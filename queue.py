class Node :
    def __init__(self,value):
        self.data = value
        self.next = None
class  Queue :
    self.front = None
    self.rear = None

    def enqueue(self,value):
        new_node = NOde(value)
        if self.front  == None:
            self.front = new_node
            self.rear= self.rear
        else:
            self.rear.next = new_node
            self.rear = new_node
    def dequeue(self):
        if self.front == None:
            return "emptyt"
        else:
            self.front = self.front.next
    def is_empty(self):
        return self.front ==None
    def size(self):
        temp = self.front
        counter = 0
        while temp != None:
            counter+=1
            temp = temp.next
        return counter
    def traverse(self):
        temp = self.front
        while temp != None:
            print(temp.data,end=' ')
            temp = temp.next
    def front_item(self):
        if self.front == None:
            return 'empty'
        else:
            return self.front.data
    def rear_item(self):
        if self.front == None:
              return 'empty'
        else:
            return self.rear.data



