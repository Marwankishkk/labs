class Queue:
    instances={}
    def __init__(self,queuelist, name, size  ):
        self.queuelist = queuelist
        self.size=size
        self.name=name
        self.instances[name]=self
    @classmethod
    def get_instance_by_name(cls, name):
        return cls.instances.get(name)

    @classmethod
    def save(cls,filename):
        with open(filename,"w")as file:
            for name,value in cls.instances.items():
                lin = f"fthe name is {name} and the values is {value.queuelist} \n"
                file.write(lin)

    @classmethod
    def load(cls, filename):
        with open(filename, "r") as file:
            for line in file:
                line=line.rstrip()
                print(line)
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self,size):
        if len(self.queuelist)>size:
            print("Queue length exceeds the maximum allowed")
        else:
            self.__size = size

    def insert(self,v):
        if len(self.queuelist) < self.size:
            self.queuelist.append(v)
        else:
            print("You cant")
    def pop(self):
        if len(self.queuelist) < 1 :
            print("The list is empty")
            return None
        else:
            return self.queuelist.pop(0)
    def is_empty(self):
        if len(self.queuelist)<1:
            return True
        else:
            return False

q1 = Queue(["marwan",22,True],"q1",5)
q1.insert(0)
print(q1.queuelist)
print(Queue.get_instance_by_name("q1").queuelist)
q2=Queue(["ahmed",12,124],"q2",9)
Queue.load("Queues.txt")