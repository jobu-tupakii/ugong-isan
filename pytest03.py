def compress_string(s):
    if not s:
        return ""

    result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1] + str(count)
            count = 1

    # 마지막 문자 처리
    result += s[-1] + str(count)

    return result

# 테스트
input_str = "aaabbccccdaa"
print(compress_string(input_str))  # 출력: a3b2c4d1a2
