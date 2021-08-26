# 이진 탐색 트리에 데이터 넣기
class NodeMgmt:
    # Node
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        # 노드를 순회
        self.current_node = self.head
        # value가 노드보다 크냐 작냐에 따라 오/왼쪽에 위치
        while True:
            # 왼쪽
            if value < self.current_node.value:
                # 이미 왼쪽에 값이 있는 경우
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                # 생성이 안되어있는 경우
                else:
                    self.current_node.left = Node(value)
                    break
            # 오른쪽
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break
                    
    # 데이터 찾기
    def search(self, value):
        self.current_node = self.head
        # 존재 확인
        while self.current_node:
            # 값이 바로 있는 경우
            if self.current_node.value == value:
                return True
            # 값이 없는 경우 노드 방향 정해줌
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        # 존재 X
        return False
    
    # 데이터 삭제
    def delete(self, value):
        # 삭제할 노드 탐색
        searched = False # 해당 값이 없다
        self.current_node = self.head # 삭제할 노드 지칭
        self.parent = self.head # 삭제할 노드의 부모 노드 지칭
        while self.current_node:
            if self.current_node.value == value:
                searched = True 
                break
            # left (작다)
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            # 같거나 크다 (right)
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right
        
        if searched == False:
            return False

        ### 이후부터 Case 나눠서 코드 작성

        # Case 1 - 삭제할 노드가 Leaf 노드인 경우
        # self.current_node가 삭제할 노드
        if self.current_node.left == None and self.current_node.right == None: # Leaf
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
            del self.current_node
        

        # Case 2 - 삭제할 노드가 자식 노드를 하나 갖고 있는 경우
        # 경우 1-1 : 삭제할 노드가 자식 노드를 왼쪽에 갖고 있을 때
        # 경우 1-2 : 삭제할 노드가 자식 노드를 오른쪽에 갖고 있을 때
        # 경우 2 : 삭제할 노드의 부모 노드가 왼/오른쪽에 있는 경우

        # 경우 1-1
        if self.current_node.left != None and self.current_node.right == None:
            # 경우 2
            if value < self.parent.value: # 부모 노드 값보다 작으므로 왼쪽에 위치
                self.parent.left = self.current_node.left # 삭제될 노드의 자식 노드 주소 값을 삭제될 노드가 갖고 있으므로 부모한테 연결해줘야함
            else:
                self.parent.right = self.current_node.left
        # 경우 1-2
        elif self.current_node.left == None and self.current_node.right != None:
            # 경우 2
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right
        

        # Case 3 - 삭제될 노드가 자식 노드를 두 개 가지고 있을 경우
        # 경우 1-1 : 삭제될 노드가 부모 노드의 왼쪽에 있을 때
        # 경우 1-2 : 삭제될 노드가 부모 노드의 오른쪽에 있을 때
        # 경우 2-1 : 삭제할 노드의 왼/오른쪽(경우 1-1/1-2에 따라) 자식 중, 가장 작은 값을 가진 노드의 자식 노드가 없을 때
        # 경우 2-2 : 삭제할 노드의 왼/오른쪽(경우 1-1/1-2에 따라) 자식 중, 가장 작은 값을 가진 노드의 자식 노드가 있을 때
        # 기본 사용 전략
        # 삭제할 노드의 오른쪽 자식 중, 가장 작은 값을 삭제할 노드의 부모 노드가 가리키도록 한다.

        # 삭제될 노드가 자식 노드를 두 개 가지고 있을 경우
        if self.current_node.left != None and self.current_node != None:
            # 경우 1-1
            if value < self.current_node.value:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                # 순회
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                self.change_node_parent.left = None # 끊기
                # 경우 2-1
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.left = self.change_node # 부모 왼쪽에 변경할 노드를 위로 올림
                self.change_node.right = self.current_node.right
                self.change_node.left = self.change_node.left
            # 경우 1-2
            else:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                # 순회
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else: # 노드가 None
                    self.change_node_parent.left = None
                self.parent.right = self.change_node # 부모 오른쪽에 변경할 노드를 위로 올림
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right
            

