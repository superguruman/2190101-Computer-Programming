first=[*input().lower()]
second=[*input().lower()]
first = [mofu for mofu in first if mofu != ' ']
second = [mofu for mofu in second if mofu != ' ']
if sorted(first) == sorted(second):
    print("YES")
else:
    print("NO")
