#lex_auth_0127438930044108801627

import sys
class Queue:
    def __init__(self,max_size):

        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if(self.__rear==self.__max_size-1):
                return True
        return False

    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False
    
    

    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])


    def get_max_size(self):
        return self.__max_size

  
def merge_queue(queue1,queue2):
    while not queue1.is_empty() & queue2.is_empty():
        if not(queue1.is_empty()):
            queue3.enqueue(queue1.dequeue())
        if not(queue2.is_empty()):
            queue3.enqueue(queue2.dequeue())
   
    return queue3

#Enqueue different values to both the queues and test your program

queue1=Queue(3)
queue2=Queue(6)
a=Queue.get_max_size(queue1)
b=Queue.get_max_size(queue2)
queue3=Queue(a+b)

queue1.enqueue(5)
queue1.enqueue(3)
queue1.enqueue(2)
queue2.enqueue('a')
queue2.enqueue('y')
queue2.enqueue('h')
queue2.enqueue('t')
queue2.enqueue('u')
queue2.enqueue('o')

merge_queue=merge_queue(queue1, queue2)
print("The elements in the merged queue are:")
merge_queue.display()
