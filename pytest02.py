def is_valid_parentheses(s):
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

# 테스트
print(is_valid_parentheses("()()"))     # True
print(is_valid_parentheses("(()())"))   # True
print(is_valid_parentheses("(()"))      # False
print(is_valid_parentheses(")("))       # False