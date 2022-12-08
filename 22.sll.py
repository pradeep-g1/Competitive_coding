class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def print_ll(self):
        if self.head is None:
            print()
        else:
            node=self.head
            while node:
                print(node.data,end="=>")
                node=node.next
            print("Null")
    def insertion(self,item,location):
        newnode=Node(item)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        else:
            if location==0:
                newnode.next=self.head
                self.head=newnode
            elif location==1:
                newnode.next=None
                self.tail.next=newnode
                self.tail=newnode
            else:
                index=0
                currnode=self.head
                while index<location-1:
                    currnode=currnode.next
                    index+=1
                nextnode=currnode.next
                currnode.next=newnode
                newnode.next=nextnode
sll=Linkedlist()
while True:
    x=int(input())
    sll.insertion(x,0)
    n=int(input())
    if n==1:
        continue
    elif n==0:
        sll.print_ll()