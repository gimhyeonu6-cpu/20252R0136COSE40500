class candidate:

    region = "전주"

    def __init__(self, name, gender, age, number, rating):

        self.name = name
        self.gender = gender
        self.age = age
        self.number = number
        self.rating = rating

    def print_info(self):
        print("후보자 정보 공개")
        print("성명 : ", self.name)
        if (self.gender == "M"):
            print("성별 : 남성")
        else:
            print("성별 : 여성")
        print("연령 :", self.age, "세")
    
class Node :

    def __init__(self,data,prev,next):
        self.data = data
        self.prev = prev
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = Node(None, None, None)
        self.tail = Node(None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    # position에 해당하는 Node 바로 다음에 value 값을 가지는 새로운  Node를 삽입 
    def node_insert(self,value,position):
        new_node = Node(value, position, position.next)
        position.next = new_node
        new_node.next.prev = new_node

    def node_delete(self, input_node):
        input_node.prev.next = input_node.next
        input_node.next.prev = input_node.prev

    def visit_all(self):
        now_node = self.head.next
        while (True):
            if (now_node.data == None):
                break
            print(now_node.data)
            npw_node = now_node.next


LL = LinkedList()
LL.node_insert("우",LL.head)
LL.node_insert("주",LL.head.next)
LL.visit_all()