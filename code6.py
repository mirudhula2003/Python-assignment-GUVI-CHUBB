import re
emails=list(input().split(' '))
valid=[]
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|co.in|in|org|net|gov|edu|info|biz)$'
for em in emails:
    if re.match(pattern,em):
        valid.append(em)
print(*valid)
