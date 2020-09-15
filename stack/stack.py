#implemented using list
stack=[]
stack.append(100)
stack.append(200)
print(stack.pop())

#using collections.deque
from collections import deque
stack=deque()
stack.append(200)
stack.append("opop")
print(stack)
print(stack.pop())

#using Queue
from queue import LifoQueue
stack=LifoQueue(maxsize=3)
print(stack.qsize())
stack.put(30)
stack.put(80)
print(stack.get())
print(stack.qsize())