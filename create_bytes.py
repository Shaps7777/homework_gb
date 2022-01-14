s = 'Hello world(мир)'
# print(type(s))
# sb = b'Hello world'
# print(type(sb))
# print(sb)
# print(s[1])
# print(sb[1])
# print(s[1:3])
# print(sb[1:3])
# for item in sb:
#     print(item)
sb = s.encode('utf-8')
print(sb)
print(type(sb))

s = sb.decode('utf-8')
print(s)
print(type(s))
