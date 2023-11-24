
text = '가힣 나는 자랑스 abcdefg ABC 1234 ㄱㄴㄷㅏ'
text_length = 0
for x in text:
    print(x, ord(x))
    if ord('가') <= ord(x) <= ord('힝'):
        text_length += 2
    else:
        text_length += 1

print(text_length)