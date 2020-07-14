from kds import kd_list
from random import choice

def write(question_list, file_name = "test.tex", mode = "w", title = "中考计算精炼", spacenum = 8):
    with open(file_name, mode) as f:
        f.write(r"\documentclass{ctexart}"\
+ r"\title{" +title + "}" +\
r"""
\begin{document}
    \maketitle
""")
        for index, question in enumerate(question_list, 1):
            f.write(f"({index}). "+f"${question}$" + r"\\"*spacenum + "\n")
        f.write("\n"+r"\end{document}")

def question_maker(a, b, n):
    string = ""
    question_list = [choice(kd_list)(a, b) for i in range(n)]
    for question in question_list:
        string = question + choice(["+", "-"]) + string
    return string[:-1]

if __name__ == "__main__":
    a = question_maker(2, 3, 4)
    print(a)