##This part is for the hackerRank
l = []
nestedList = []
s = set()
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append(name)
        l.append(score)
        s.add(score)
        nestedList.append(l)
        l = []
list = (sorted(s))
lowestElement = list[1]
nestedList.sort()
for i in nestedList:
        if lowestElement == i[1]:
                print(i[0])

#####################################################################

####****This part is also worked in any platform****####
# l = []
# nestedList = []
# s = set()
# for i in range(4):
#         name = input()
#         score = float(input())
#         l.append(name)
#         l.append(score)
#         s.add(score)
#         nestedList.append(l)
#         l = []
# list = (sorted(s))
# lowestElement = list[1]
# nestedList.sort()
# for i in nestedList:
#         if lowestElement == i[1]:
#                 print(i[0])

