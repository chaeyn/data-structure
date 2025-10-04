from array_stack import ArrayStack
from eval_postfix import evalPostfix # 중위 -> 후위

# 연산자의 우선순위 계산 함수
def precedence(op):
    if op == "(" or op == ")": return 0
    elif op == "+" or op == "-": return 1
    elif op == "*" or op == "/": return 2
    else: return -1

def Infix2Postfix(expr):
    s = ArrayStack(100)
    output = [] # 후위 표기식 저장한 출력 리스트

    for term in expr:
        if term == "(": # term이 여는 괄호이면 스택에 삽입
            s.push(term)
        elif term == ")": # term이 닫는 괄호이면
            while not s.isEmpty(): # 스택이 빌 때 까지
                op = s.pop() # s.pop() 실행
                if op == "(": # 여는 괄호가 아니라면 연산자이므로
                    break # ()는 후위 표기 결과에 포함 X
                else:
                    output.append(op) # 후위 표기 리스트에 추가
        elif term in "+-*/": # term이 연산자라면
            while not s.isEmpty(): # 스택이 비어있지 않다면
                op = s.peek()
                if precedence(term) <= precedence(op): # 현재 연산자와 스택 상단의 연산자의 우선순위 비교, 스택 상단의 연산자 우선순위가 같거나 높으면
                    output.append(op) # 후위 표기식에 추가하고
                    s.pop() # 스택에서 꺼낸다
                else : break
            s.push(term)
        else: # term이 피연산자이면 후위표기식에 추가
            output.append(term)
    while not s.isEmpty():
        output.append(s.pop()) # expr 리스트 값을 모두 확인한 후 스택에 남은 모든 요소들을 꺼내 순서대로 출력
    return output

if __name__ == "__main__":
    print('중위표기식 후위표기 변환\n')

    infix1 = ['8', '/', '2', '-', '3', '+', '(', '3', '*', '2', ')']
    infix2 = ['1', '/', '2', '*', '4', '*', '(', '1', '/', '4', ')']

    postfix1 = Infix2Postfix(infix1)
    postfix2 = Infix2Postfix(infix2)

    result1 = evalPostfix(postfix1)
    result2 = evalPostfix(postfix2)

    print('  중위표기: ', infix1)
    print('  후위표기: ', postfix1)
    print('  계산결과: ', result1, end='\n\n')

    print('  중위표기: ', infix2)
    print('  후위표기: ', postfix2)
    print('  계산결과: ', result2)