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