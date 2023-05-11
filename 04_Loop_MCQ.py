answer=input()
student=input()
correct=0
if len(student) != len(answer):
  print('Incomplete answer')
else:
  for arm in range(len(answer)):
    if student[arm] == answer[arm]:
      correct += 1
  print(correct)