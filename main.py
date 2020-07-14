from kds import kd_list
from writer import write, question_maker
from random import choice
num = 100
a_list = [2, 3]  # 二次根式下数列表
b_list = [2, 3]  # 分母列表
n_list = [3, 4, 5]
question_list = []
while True:
    if num == 0:#计数器
        break
    num -= 1
    a = choice(a_list)
    b = choice(b_list)
    n = choice(n_list)
    question_list.append(question_maker(a = a, b = b, n = n))
print(question_list)
write(question_list)

    

