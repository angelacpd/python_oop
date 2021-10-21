N = int(input())
p = input()
persons = p.split(' ')

lowest_pos = 0
for i in range(0, N, 1):
    if i == 0:
        lowest = int(persons[0])
        continue
    if int(persons[i]) < lowest:            
        lowest = int(persons[i])
        lowest_pos = i
print(lowest_pos + 1)
