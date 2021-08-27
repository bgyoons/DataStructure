# 힙 클래스 구현
class Heap:
    def __init__(self, data):
        # 힙은 배열로
        self.heap_array = list()
        # 맨 처음 데이터는 None, 인덱스 번호 1부터 시작
        self.heap_array.append(None)
        self.heap_array.append(data)


    # 데이터 입력하는 과정
    # 1. 이진트리처럼 왼쪽부터 쌓아가는 과정
    # 2. 쌓여진 맨 끝에 있는 데이터를 위와 바꿔가는 과정

    # 상위 노드와의 관계 크기가 누가 더 큰지, 혹은 이미 루트 노드라서 바꿀 필요가 없는지 판별하는 메소드
    # 부모 노드보다 더 크거나 루트 노드가 아닐 경우 => True => 부모노드와 위치 바꿔줌
    def move_up(self, inserted_idx):
        # 이미 루트 노드 (할 필요 X)
        if inserted_idx <= 1:
            return False
        
        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    # 완전 이진트리에 맞춰 데이터 삽입
    def insert(self, data):
        # 데이터가 없는 경우 초기화(방어코드)
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        
        self.heap_array.append(data)
        
        inserted_idx = len(self.heap_array) -1
        
        # True => 바꿔줌
        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            # 부모 노드와 바꿔줘야 함(swap)
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
            inserted_idx = parent_idx
        return True
    

    # 데이터 삭제 (Max Heap)
    # 루트 노드에서 최대 힙인 경우 최대를 뽑아내고 루트를 삭제
    # 1. 맨 위에 루트 노드를 삭제
    # 2. 삭제한 루트 노드를 채워가면서 힙의 구조를 만들기

    def move_down(self, poped_idx):
        left_child_popped_idx = poped_idx * 2  # 왼쪽 자식 노드
        right_child_popped_idx = poped_idx * 2 + 1  # 오른쪽 자식 노드

        # Case 1 왼쪽 자식 노드도 없을 때
        if left_child_popped_idx >= len(self.heap_array):
            return False
        # Case 2 오른쪽 자식 노드만 없을 때
        elif right_child_popped_idx >= len(self.heap_array):
            # 왼쪽 자식이 더 큰 경우
            if self.heap_array[poped_idx] < self.heap_array[left_child_popped_idx]:
                return True
            else:
                return False
        # Case 3 왼/오 두 자식 노드 모두 있을 때
        else:
            # 왼/오 자식끼리 크기 비교
            if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                # 왼쪽 자식과 부모 노드 크기 비교
                if self.heap_array[poped_idx] < self.heap_array[left_child_popped_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[poped_idx] < self.heap_array[right_child_popped_idx]:
                    return True
                else:
                    return False
        
    def pop(self):
        if len(self.heap_array) <= 1:
            return None

        returned_data = self.heap_array[1] # 인덱스는 1부터 시작, [1]은 항상 루트
        # 맨 마지막에 입력된 데이터가 루트에 올라갔을 때 자식 노드와 비교해서 값 비교(자식 노드보다 클 때, 자식 노드가 없을 때까지)
        # 마지막 데이터 루트로 올리기
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        poped_idx = 1 # 위로 올라간 데이터(루트)

        while self.move_down(poped_idx):
            left_child_popped_idx = poped_idx * 2  # 왼쪽 자식 노드
            right_child_popped_idx = poped_idx * 2 + 1  # 오른쪽 자식 노드

            # Case 2 오른쪽 자식 노드만 없을 때
            if right_child_popped_idx >= len(self.heap_array):
                # 왼쪽 자식이 더 큰 경우
                if self.heap_array[poped_idx] < self.heap_array[left_child_popped_idx]:
                    self.heap_array[poped_idx], self.heap_array[left_child_popped_idx]= self.heap_array[left_child_popped_idx], self.heap_array[poped_idx]
                    poped_idx = left_child_popped_idx
            # Case 3 왼/오 두 자식 노드 모두 있을 때
            else:
                # 왼/오 자식끼리 크기 비교
                if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                    # 왼쪽 자식과 부모 노드 크기 비교
                    if self.heap_array[poped_idx] < self.heap_array[left_child_popped_idx]:
                        self.heap_array[poped_idx], self.heap_array[left_child_popped_idx]= self.heap_array[left_child_popped_idx], self.heap_array[poped_idx]
                        poped_idx = left_child_popped_idx
                else:
                    if self.heap_array[poped_idx] < self.heap_array[right_child_popped_idx]:
                        self.heap_array[poped_idx], self.heap_array[right_child_popped_idx]= self.heap_array[right_child_popped_idx], self.heap_array[poped_idx]
                        poped_idx = right_child_popped_idx
                        
        return returned_data





### 힙 클래스 구현
heap = Heap(15)
print(heap.heap_array) 
# [None, 15]

### 데이터 입력
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array) 
# [None, 20, 10, 15, 5, 4, 8]

### 데이터 삭제
heap.pop()
print(heap.heap_array) 
# [None, 15, 10, 8, 5, 4]