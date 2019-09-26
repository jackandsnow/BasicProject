class Stack:
    """
    Sequential Stack implement
    """

    def __init__(self):
        """
        initialize an empty Stack, __stack means it's a private member
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


class LinkNode:
    """
    Link Node definition
    """

    def __init__(self):
        self.data = None
        self.next = None


class LinkStack:
    """
    Link Stack implement
    """

    def __init__(self):
        """
        initialize an empty Link Stack
        """
        self.__link_stack = LinkNode()

    def top(self):
        """
        get the top element of Link Stack
        :return: if Link Stack is empty return None, else return the top element
        """
        return None if self.isEmpty() else self.__link_stack.next.data

    def push(self, obj):
        """
        push an element into Link Stack
        :param obj: object to be pushed
        """
        node = LinkNode()
        node.data = obj
        node.next = self.__link_stack.next
        self.__link_stack.next = node

    def pop(self):
        """
        pop the top element from Link Stack
        :return: if Link Stack is empty return None, else return the popped element
        """
        if self.isEmpty():
            return None
        else:
            next_node = self.__link_stack.next
            self.__link_stack.next = next_node.next
            return next_node.data

    def clear(self):
        """
        clear the whole Link Stack
        """
        self.__link_stack = LinkNode()

    def isEmpty(self):
        """
        judge the Link Stack is empty or not
        :return: bool value
        """
        return self.__link_stack.next is None

    def length(self):
        """
        get the length of Link Stack
        :return:
        """
        count = 0
        curr_node = self.__link_stack.next
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count
