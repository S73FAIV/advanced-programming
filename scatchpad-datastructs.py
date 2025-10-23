# Let's prepare a LinkedList class, with an internal class called Element.
# Remember that each element, apart from its value, has a reference to the previous element, and that in Python, lists are passed by reference
# Prepare the methods for that class to create, insert list at beginning, and find out its length.
# It may be interesting to keep track of the last one and the length.


# class Element():
#     def __init__(self, value: int) -> None:
#         self.value = value
#         self.previous = None

#     def __str__(self) -> str:
#         if self.previous is None:
#             return "HEAD: Element with Val=" + str(self.value)
#         return "Element with Val=" + str(self.value) + "; Previous: -> \n" + str(self.previous)

#     def find_length(self) -> int:
#         if self.previous is None:
#             return 1
#         else:
#             return self.previous.get_length() +1

#     def get_head(self):
#         if self.previous is None:
#             return self
#         else:
#             return self.previous.find_head()

#     def insert_at_beginning(self, element) -> None:
#         if self.previous is not None:
#             return self.previous.insert_at_beginning(element)
#         if self.previous is None:
#             self.previous = element

# class BackwardLinkedList():

#     end: Element

#     def __init__(self, inital_value: int) -> None:
#         self.end = Element(value=inital_value)

#     def __str__(self) -> str:
#         return str(self.end)

#     def get_length(self) -> int:
#         return self.end.find_length()

#     def insert_at_head(self, element) -> None:
#         self.end.insert_at_beginning(element=element)

#     def append_bllist_at_beginning(self, list_to_append):
#         self.end.get_head().previous = list_to_append.end


# bll = BackwardLinkedList(1)
# for i in range(10, 15):
#     new_element = Element(i)
#     bll.insert_at_head(new_element)

# second_bll = BackwardLinkedList(2)
# for i in range(100, 150, 10):
#     new_element = Element(i)
#     second_bll.insert_at_head(new_element)

# print(bll)
# print(second_bll)

# bll.append_bllist_at_beginning(second_bll)
# print(bll)

################################


class Operator:
    """This class represents an operador in a calulation"""

    operator: str
    valid_operators = ["*", "/", "+", "-", "(", ")"]
    binary_operators = ["*", "/", "+", "-"]

    def __init__(self, operator: str) -> None:
        if operator not in self.valid_operators:
            raise TypeError("Invalid Operator")
        self.operator = operator

    def has_higher_preference_as(self, other_operator) -> bool:
        """Returns true, if the this operator has higher preference than the other"""
        return (
            self.valid_operators.index(self.operator) // 2
            < self.valid_operators.index(other_operator) // 2
        )

    def binario(self) -> bool:
        return self.operator in self.binary_operators

    def complete_operation(self, left_operand: float, right_operand: float) -> float:
        return eval(str(left_operand) + self.operator + str(right_operand))


from collections import deque


class Evaluator:
    numbers: deque[float]
    operators: deque[Operator]
    result: float

    def __init__(self, expression: str) -> None:
        self.expression = []
        self.numbers = deque()
        self.operators = deque()
        for string in expression.split():
            try:
                operador = Operator(string)
                if string == "(":
                    self.operators.append(operador)
                elif len(self.operators) == 0 or operador.has_higher_preference_as(
                    self.operators[-1]
                ):
                    self.operators.append(operador)
                    self.expression.append(Operator(string))
                # if the operator has lower priority we need to do some calculations
                else: self.lower_priority(operador)
            except TypeError:
                self.numbers.append(float(string))
  
        while len(self.operators) > 0:
            operador = self.operators.pop()
            right_number = self.numbers.pop()
            left_number = self.numbers.pop()
            self.numbers.append(operador.complete_operation(left_number, right_number))

        self.result = self.numbers.pop()


    def lower_priority(self, operator: Operator) -> None:
        """Function that handles the case, if the incoming operator has lower priority than the previous"""
        while not operator.has_higher_preference_as(self.operators[-1]):
            last_operator = self.operators.pop()
            if last_operator.binario():
                self.numbers.append(last_operator.complete_operation(self.numbers.pop(), self.numbers.pop()))
            else: # lets hope we are talking about closing parenthesis
                if operator.operator == ")" and last_operator.operator == "(":
                    return 
                else: 
                    raise Exception()

