from kds import kd_list
from fuctions import write, question_maker
from random import choice
num = i = 1000 #生成的题目个数
a_list = [2, 3]  # 二次根式下数列表
b_list = [2, 3]  # 分母列表
n_list = [3, 4, 5] #每一道题目可能的项数
question_list = [] #题目列表
while True:
    if i == 0:#计数器
        break
    i -= 1
    a = choice(a_list)
    b = choice(b_list)
    n = choice(n_list)
    question_list.append(question_maker(a = a, b = b, n = n)) #产生题目

write(question_list = question_list, title = f"中考数学{num}练")

    

