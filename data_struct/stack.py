class Stack:

    def __init__(self):
        """
        initial an empty Stack, __stack means it's a private member
        """
        self.__stack = []

    def top(self):
        """
        get the top element of Stack
        :return: if Stack is empty return None, else return the top element
        """
        return None if self.isEmpty() else self.__stack[-1]

    def push(self, obj):
        """
        push an element into Stack
        :param obj: object to be pushed
        """
        self.__stack.append(obj)

    def pop(self):
        """
        pop the top element from Stack
        :return: if Stack is empty return None, else return the popped element
        """
        return None if self.isEmpty() else self.__stack.pop()

    def clear(self):
        """
        clear the whole Stack
        """
        self.__stack.clear()

    def isEmpty(self):
        """
        judge the Stack is empty or not
        :return: bool value
        """
        return self.length() == 0

    def length(self):
        """
        get the length of Stack
        :return:
        """
        return len(self.__stack)
