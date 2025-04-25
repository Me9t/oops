class stack:
    def __init__(self):
        self.items=[]
        
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def is_empty(self):
        return self.items==0
        
    def length(self):
        return len(self.items)
    
    
s=stack()

s.push('apple')
s.push('mango')
print(f"stack:{s.items}")

print(f"top content{s.peek()}")

print(f"popped item={s.pop()}")

print(f"current stack:{s.items}")

print(f"is tack empty? {s.is_empty()}")

print(f"length of stack: {s.length()}")

        
        
        
        