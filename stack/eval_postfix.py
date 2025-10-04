from array_stack import ArrayStack

def evalPostfix(expr): # 매개변수는 연산자와 피연산자가 모두 문자열로 저장된 리스트
    s = ArrayStack(100)
    for token in expr:
        if token in "+-*/": # token이 연산자이면 -> 스택에서 두 개의 피연산자를 순서대로 꺼낸다
            val2 = s.pop()
            val1 = s.pop()
            if (token == "+") : s.push(val1 + val2)
            elif (token == "-") : s.push(val1 - val2)
            elif (token == "*") : s.push(val1 * val2)
            elif (token == "/") : s.push(val1 / val2)
        else:
            s.push(float(token)) # token이 피연산자이면 -> 문자열을 실수로 변환해서 스택에 저장
    return s.pop()

if __name__ == "__main__":
    expr1 = input("연산자와 피연산자를 공백을 구분하여 입력하시오.").split()

    expr2 = ["1", "2", "/", "4", "*", "1", "4", "/", "*"]

    print(expr1, ' ---> ',  evalPostfix(expr1))
    print(expr2, ' ---> ',  evalPostfix(expr2))