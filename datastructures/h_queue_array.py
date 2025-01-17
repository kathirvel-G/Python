class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = capacity-1
        self.Q = [None] * capacity
        self.size = 0

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def EnQueue(self, item):
        if self.size == self.capacity:
            print("full")
            return
        self.rear = (self.rear+1)%(self.capacity)
        self.Q[self.rear] = item
        self.size = self.size + 1
        print(item)

    def DeQueue(self):
        if self.size == 0:
            print("Queue is empty")
            return
        print(self.Q[self.front])
        self.front = (self.front+1)%(self.capacity)
        print("self.front is ", self.front)
        self.size = self.size-1

    def que_front(self):
        if self.isEmpty():
            print("Queue is empty")

        print("Front item is", self.Q[self.front])

    # Function to get rear of queue
    def que_rear(self):
        if self.isEmpty():
            print("Queue is empty")
        print("Rear item is", self.Q[self.rear])


queue = Queue(15)
queue.EnQueue(10)
queue.EnQueue(20)
queue.EnQueue(30)
queue.EnQueue(40)
queue.DeQueue()
queue.DeQueue()
queue.DeQueue()
queue.DeQueue()
# queue.DeQueue()
# queue.que_front()
# queue.que_rear()