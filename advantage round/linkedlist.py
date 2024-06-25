class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linklist:
    def __init__(self) -> None:
        self.head=None

    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def inafter(self,prev_node,new_data):
        if prev_node is None:
            print("prv is needed in llinklist")
            return
        new_node=Node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node

    def append(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node




    def printing(self):
        temp=self.head
        while(temp):
            print(temp.data,end=",")
            temp=temp.next

       

if __name__=='__main__':

    list=linklist()

    list.head=Node(57)

    sec=Node(6)
    th=Node(785)
    four=Node(33)

    list.head.next=sec
    sec.next=th
    th.next=four

    list.push(5)
    list.push(88)
    list.printing()

    
    list.inafter(list.head.next, 8907)
    list.append(777)
    print(end="\n")
    list.printing()
    
    

    