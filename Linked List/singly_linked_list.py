"""

Linked List: In array we have contigenious memory allocation,array size is fix in other programing language except python, so we have to make array with the size that all the elements can be stored. This is the problem in array. To solve this problem linked list come in picture by providing feature of allocate memory at run time. 

"""

"""
Array:
_________________________________________
|___|___|___|___|___|___|___|___|___|___|

<---------------------------------------->


"""

"""
Singly Linked List:

                     
        _________________________
head    |___________|___________|           

        <----------------------->
                node   
        info
        <----------->
                    next location 
                    address
                    <----------->



    100         200         150
_______     _______      _______
|__|__|     |__|__|      |__|__| 

"""

"""
Pointer(reference variable in python): Pointer in singly list is a reference variable that stores the address of next node that enabling travelsal of list.

head.info
head.next

We can extend this till we have memory, insertion at middle, insertion at begining, insertion at end, searching, sorting, but not go to reverse(this is drawback only forward direction)
"""

# code of singly list

class Node:
    def __init__(self,info,next=None):
        self.data = info
        self.next = next

class SinglyLinkedList:
    def __init__(self,head=None):
        self.head = head
    
    def insertAtEnd(self,value):
        temp = Node(value)
        if (self.head != None):
            t1 = self.head
            while (t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def insertAtBegining(self,value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def insertAtMiddle(self,value,x):
        temp = Node(value)
        t1 = self.head
        while (t1.next != None):
            if(t1.data == x):
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next
         

    def deleteLL(self,value):
        t1 = self.head
        prev = t1
        if (t1.data == value):
            self.head = t1.next
        while (t1.next !=None):
            if (t1.data == value):
                prev.next = t1.next
                break
            else:
                prev = t1
                t1 = t1.next
        if (t1.data == value):
            prev.next = None

    def printLL(self):
        t1 = self.head
        while (t1.next != None):
            print(t1.data)
            t1 = t1.next 
        print(t1.data)
               
obj = SinglyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtBegining(5)
obj.insertAtMiddle(40,20)
obj.deleteLL(5)
obj.printLL()