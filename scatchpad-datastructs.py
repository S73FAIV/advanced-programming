# Let's prepare a LinkedList class, with an internal class called Element. 
# Remember that each element, apart from its value, has a reference to the previous element, and that in Python, lists are passed by reference
# Prepare the methods for that class to create, insert list at beginning, and find out its length. 
# It may be interesting to keep track of the last one and the length.


class Element():
    def __init__(self, value: int) -> None:
        self.value = value
        self.previous = None
    
    def __str__(self) -> str:
        if self.previous is None:
            return "HEAD: Element with Val=" + str(self.value)
        return "Element with Val=" + str(self.value) + "; Previous: -> \n" + str(self.previous)

    def find_length(self) -> int:
        if self.previous is None:
            return 1
        else:
            return self.previous.get_length() +1
    
    def get_head(self):
        if self.previous is None:
            return self
        else:
            return self.previous.find_head()
    
    def insert_at_beginning(self, element) -> None:
        if self.previous is not None:
            return self.previous.insert_at_beginning(element)
        if self.previous is None:
            self.previous = element

class BackwardLinkedList():

    end: Element

    def __init__(self, inital_value: int) -> None:
        self.end = Element(value=inital_value)

    def __str__(self) -> str:
        return str(self.end)

    def get_length(self) -> int:
        return self.end.find_length()
    
    def insert_at_head(self, element) -> None:
        self.end.insert_at_beginning(element=element)

    def append_bllist_at_beginning(self, list_to_append):
        self.end.get_head().previous = list_to_append.end



bll = BackwardLinkedList(1)
for i in range(10, 15):
    new_element = Element(i)
    bll.insert_at_head(new_element)

second_bll = BackwardLinkedList(2)
for i in range(100, 150, 10):
    new_element = Element(i)
    second_bll.insert_at_head(new_element)

print(bll)
print(second_bll)

bll.append_bllist_at_beginning(second_bll)
print(bll)

