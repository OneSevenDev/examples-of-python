
class Adder:
    def __init__(self):
        self.sum = 0
    def add(self, value):
        self.sum += value

acc = Adder()

for i in range(99):
    acc.add(i)

print(acc.sum)

"""
Learning to page: 'https://www.solvetic.com/tutoriales/article/919-abstraccion-en-python/'
"""

# fibs = [0, 1]
# # for i in range(8):
# #     fibs.append(fibs[-2] + fibs[-1])

# num = input('How many Fibonacci number do you want?')
# for i in range(int(num)-2):
#     fibs.append(fibs[-2] + fibs[-1])

# print(fibs)