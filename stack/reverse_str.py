from array_stack import ArrayStack

s = ArrayStack(50)

msg = input("문자열 입력: ")
for c in msg:
    s.push(c) # 문자열의 각 문자 c를 스택에 삽입

print("문자열 출력: ", end="")
while not s.isEmpty():
    print(s.pop(), end="") # 스택이 공백이 아니라면 하나의 요소를 꺼내서 출력
print()