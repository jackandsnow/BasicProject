class Queue:
    """
    Sequential Queue implement
    """

    def __init__(self):
        """
        initialize an empty Queue, __queue means it's a private member
        """
        self.__queue = []

    def first(self):
        """
        get the first element of Queue
        :return: if Queue is empty return None, else return the first element
        """
        return None if self.isEmpty() else self.__queue[0]

    def enqueue(self, obj):
        """
        enqueue an element into Queue
        :param obj: object to be enqueued
        """
        self.__queue.append(obj)

    def dequeue(self):
        """
        dequeue the first element from Queue
        :return: if Queue is empty return None, else return the dequeued element
        """
        return None if self.isEmpty() else self.__queue.pop(0)

    def clear(self):
        """
        clear the whole Queue
        """
        self.__queue.clear()

    def isEmpty(self):
        """
        judge the Queue is empty or not
        :return: bool value
        """
        return self.length() == 0

    def length(self):
        """
        get the length of Queue
        :return:
        """
        return len(self.__queue)


class PriorQueue:
    """
    Priority Queue implement
    """

    def __init__(self, objs=[]):
        """
        initialize a Priority Queue, and the default queue is empty
        :param objs: object list for initializing
        """
        self.__prior_queue = list(objs)
        # sort from maximum to minimum, and the minimum has the highest priority
        # so that the efficiency of "dequeue" will be O(1)
        self.__prior_queue.sort(reverse=True)

    def first(self):
        """
        get the highest priority element of Priority Queue, O(1)
        :return: if Priority Queue is empty return None, else return the highest priority element
        """
        return None if self.isEmpty() else self.__prior_queue[-1]

    def enqueue(self, obj):
        """
        enqueue an element into Priority Queue, O(n)
        :param obj: object to be enqueued
        """
        index = self.length()
        while index > 0:
            if self.__prior_queue[index - 1] < obj:
                index -= 1
            else:
                break
        self.__prior_queue.insert(index, obj)

    def dequeue(self):
        """
        dequeue the highest priority element from Priority Queue, O(1)
        :return: if Priority Queue is empty return None, else return the dequeued element
        """
        return None if self.isEmpty() else self.__prior_queue.pop()

    def clear(self):
        """
        clear the whole Priority Queue
        """
        self.__prior_queue.clear()

    def isEmpty(self):
        """
        judge the Priority Queue is empty or not
        :return: bool value
        """
        return self.length() == 0

    def length(self):
        """
        get the length of Priority Queue
        :return:
        """
        return len(self.__prior_queue)

