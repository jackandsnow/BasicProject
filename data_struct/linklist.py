class SingleLinkNode:
    """
    Single Link Node definition
    """

    def __init__(self, data=None):
        self.data = data
        self.next = None


class SingleLinkList:
    """
    Single Link List implement
    """

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
            length = self.length()
            index = index if index >= 0 else length + index
            # insert at the first position
            if index == 0:
                curr = self.__head
                node.next = curr
                self.__head = node
            elif 0 < index < length:
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

        length = self.length()
        index = index if index >= 0 else length + index
        if 0 <= index < length:
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
        prev = None
        while curr:
            back = curr.next
            curr.next = prev
            prev = curr
            curr = back
        self.__head = prev

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
        self.prev = None
        self.next = None


class DoubleLinkList:
    """
    Double Link List implement
    """

    def __init__(self):
        """
        Initialize Double Link List
        """
        self.__head = DoubleLinkNode()
        self.__tail = DoubleLinkNode()
        self.__head.next = self.__tail
        self.__tail.prev = self.__head

    def append(self, obj):
        """
        append an element at tail
        :param obj: object for appending
        """
        node = DoubleLinkNode(obj)
        prev_node = self.__tail.prev
        self.__tail.prev = node
        node.next = self.__tail
        node.prev = prev_node
        prev_node.next = node

    def insert(self, obj, index):
        """
        insert an element at specific position
        :param obj: object for inserting
        :param index: target position
        """
        node = DoubleLinkNode(obj)
        length = self.length()
        index = index if index >= 0 else length + index
        # insert at the first position
        if index == 0:
            back = self.__head.next
            self.__head.next = node
            node.prev = self.__head
            node.next = back
            back.prev = node
        elif 0 < index < length:
            count = 1
            curr = self.__head
            while curr.next != self.__tail:
                if count == index:
                    node.prev = curr
                    node.next = curr.next
                    curr.next.prev = node
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
        else:
            curr = self.__head.next
            while curr != self.__tail:
                if curr.data == obj:
                    prev_node = curr.prev
                    prev_node.next = curr.next
                    curr.next.prev = prev_node
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

        length = self.length()
        index = index if index >= 0 else length + index
        if 0 <= index < length:
            count = 0
            curr = self.__head.next
            while curr != self.__tail:
                if count == index:
                    return curr.data
                else:
                    count += 1
                    curr = curr.next
        else:
            return None

    def clear(self):
        """
        clear the whole Double Link List
        """
        self.__head.next = self.__tail
        self.__tail.prev = self.__head

    def reverse(self):
        """
        reverse the Double Link List
        """
        if self.isEmpty() or self.length() == 1:
            return

        prev = self.__tail
        curr = self.__head.next
        while curr != self.__tail:
            back = curr.next
            if back != self.__tail:
                curr.prev = back
            else:
                # deal with head
                curr.prev = self.__head
                self.__head.next = curr

            curr.next = prev
            # deal with tail
            if prev == self.__tail:
                self.__tail.prev = curr
            prev = curr
            curr = back
        self.__head.prev = self.__tail.next = None

    def length(self):
        """
        get the length of Double Link List
        :return:
        """
        count = 0
        curr = self.__head
        while curr.next != self.__tail:
            count += 1
            curr = curr.next
        return count

    def isEmpty(self):
        """
        judge the Double Link List is empty or not
        :return: bool value
        """
        return self.__head.next == self.__tail

    def print_all(self):
        """
        print all elements of Double Link List
        """
        element = []
        curr = self.__head.next
        while curr != self.__tail:
            element.append(curr.data)
            curr = curr.next
        print(element)
