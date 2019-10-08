class SingleLinkNode:
    """
    Single Link Node definition
    """

    def __init__(self, data=None):
        self.data = data
        self.next = None


class SingleLinkList:

    def __init__(self):
        """
        Initialize an empty pointer
        """
        self.__head = None

    def append(self, obj):
        """
        append an element at tail
        :param obj: object for appending
        """
        node = SingleLinkNode(obj)
        if self.isEmpty():
            self.__head = node
        else:
            curr = self.__head
            while curr.next:
                curr = curr.next
            curr.next = node

    def insert(self, obj, index):
        """
        insert an element at specific position
        :param obj: object for inserting
        :param index: target position
        """
        node = SingleLinkNode(obj)
        if self.isEmpty():
            self.__head = node
        else:
            # insert at the first position
            if index == 0:
                curr = self.__head
                node.next = curr
                self.__head = node
            elif 0 < index < self.length():
                count = 1
                curr = self.__head
                while curr.next:
                    if count == index:
                        node.next = curr.next
                        curr.next = node
                        break
                    else:
                        count += 1
                        curr = curr.next
            # if index is out of range, insert at last position
            else:
                self.append(obj)

    def remove(self, obj):
        """
        remove the first element of target object
        :param obj: target object
        """
        if self.isEmpty():
            pass
        # remove the first element
        elif self.__head.data == obj:
            self.__head = self.__head.next
        else:
            curr = self.__head
            while curr.next:
                if curr.next.data == obj:
                    curr.next = curr.next.next
                    break
                else:
                    curr = curr.next

    def getValue(self, index):
        """
        get value of specific position
        :param index: specific position
        :return: value
        """
        if self.isEmpty():
            return None

        if 0 <= index < self.length():
            count = 0
            curr = self.__head
            while curr:
                if count == index:
                    return curr.data
                else:
                    count += 1
                    curr = curr.next
        else:
            return None

    def clear(self):
        """
        clear the whole Single Link List
        """
        self.__head = None

    def reverse(self):
        """
        reverse the Single Link List
        """
        if self.isEmpty() or self.length() == 1:
            return

        curr = self.__head
        pre = None
        while curr:
            back = curr.next
            curr.next = pre
            pre = curr
            curr = back
        self.__head = pre

    def length(self):
        """
        get the length of Single Link List
        :return:
        """
        count = 0
        curr = self.__head
        while curr:
            count += 1
            curr = curr.next
        return count

    def isEmpty(self):
        """
        judge the Single Link List is empty or not
        :return: bool value
        """
        return self.__head is None

    def print_all(self):
        """
        print all elements of Single Link List
        """
        element = []
        curr = self.__head
        while curr:
            element.append(curr.data)
            curr = curr.next
        print(element)


class DoubleLinkNode:
    """
    Double Link Node definition
    """

    def __init__(self, data=None):
        self.data = data
        self.pre = None
        self.next = None


class DoubleLinkList:

    def __init__(self):
        pass
