from array_stack import ArrayStack

def checkBrackets(statement):
    stack = ArrayStack(100)
    for ch in statement:
        if ch == "{" or ch == "[" or ch == "(": # ch가 열리는 괄호이면
            stack.push(ch) # 스택에 삽입
        elif ch == "}" or ch == "]" or ch == ")": # 닫히는 괄호인지 검사
            if stack.isEmpty(): # 스택이 공백이면 조건 위반
                return False
            else:
                left = stack.pop()
                if ((ch == "}" and left != "{") or
                    ch == "]" and left != "[" or
                    ch == ")" and left != "(") :
                    return False # 스택에서 괄호를 꺼내 ch와 짝이 맞는지 비교, 짝이 맞지 않으면 조건 위반
    return stack.isEmpty()

if __name__ == "__main__":
    s1 = "{ A[ (i+1) ] = 0; } "
    s2 = "if( (i==0) && (j==0)"
    s3 = "A[ ( i+1 ] ) = 0;   "
    print(s1, " ---> ", checkBrackets(s1))
    print(s2, " ---> ", checkBrackets(s2))
    print(s3, " ---> ", checkBrackets(s3))