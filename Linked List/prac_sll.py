# create class node add data and next in it

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

# create a class SinglyLL and add head and deafualt null
class SinglyLL:
    def __init__(self):
        self.head = None

    def insertatEnd(self,value):
        temp = Node(value)
        if self.head == None:
            self.head = temp
            return temp.data
        else:
            t1 = self.head

            while t1.next is not None:
                t1 = t1.next
            t1.next = temp
            return temp.data

        

obj = SinglyLL()
print(obj.insertatEnd(10))
print(obj.insertatEnd(20))