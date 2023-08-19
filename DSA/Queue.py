# Queue implementation in Python

class Queue:

    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display  the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


q = Queue()
q.enqueue("Minecraft")
q.enqueue("CSGO")
q.enqueue("VALORANT")
q.enqueue("Call of Duty")
q.enqueue("Halo")

q.display()

q.dequeue()

print("After removing an element")
q.display()