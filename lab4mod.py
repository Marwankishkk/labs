
class Queue:

    def __init__(self,queuelist):
        self.queuelist = queuelist


    def insert(self,v):
        self.queuelist.append(v)

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



class Queuev2(Queue):
    instances = {}
    def __init__(self, queuelist, name, size):
        super().__init__(queuelist)
        self.size = size
        self.name = name
        self.instances[name] = self



    @classmethod
    def save(cls, filename):
        with open(filename, "w") as file:
            for name, value in cls.instances.items():
                lin = f"fthe name is {name} and the values is {value.queuelist} \n"
                file.write(lin)

    @classmethod
    def load(cls, filename):
        with open(filename, "r") as file:
            for line in file:
                line = line.rstrip()
                print(line)

    @classmethod
    def get_instance_by_name(cls, name):
        return cls.instances.get(name)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if len(self.queuelist) > size:
            print("Queue length exceeds the maximum allowed")
        else:
            self.__size = size
    def insert(self,v):
        if len(self.queuelist) < self.size:
            self.queuelist.append(v)
        else:
            print("You cant")
q2=Queuev2([2,3,2,3,23],"q2",4)
print(q2.queuelist)
Queuev2.save("Queues.txt")