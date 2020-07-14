from random import choice

class connecter:
    def __init__(self, a, b, sign = "+"):
        self.a = a
        self.b = b
        self.sign = sign
    def __repr__(self):
        return (self.a.__repr__() + self.sign + self.b.__repr__())
class kds:
    """考点的父类,用于格式化考点类的行为"""
    def __init__(selfa, a = 0 , b = 0):
        self.tex = ""
    def __repr__(self):
        return self.tex
    def __add__(self, other):
        return repr(self) + str(other)
    def __radd__(self, other):
        return repr(self) + str(other)

###############分割线#################

class ocf(kds):
    def __init__(self, a = 0, b = 0):
        """
        本考点用于生成负数偶次方
        :param a: 二次根式下数
        :param b: 分母
        """
        basiclist = ["-1", "-2", "-3"]
        num1 = choice(basiclist)
        self.tex = f"({num1})^2"

class lcf(kds):
    def __init__(self, a = 0 , b = 0):
        """
        本考点用于生成零次方
        :param a: 二次根式下数
        :param b: 分母
        """
        bignumber = ["2019", "2020", "2021"]
        sign = ["+", "-"]
        pi = r"\pi"
        basiclist = bignumber + [pi] + [m + choice(sign) + pi for m in bignumber] +\
                    [f"{m}^{n}" for m in bignumber for n in range(2, 10)]
        self.tex = f"({choice(basiclist)})^0"

class ecgs(kds):
    def __init__(self, a = 0, b = 0):
        """
        本考点用于生成二次根式
        :param a: 二次根式下数
        :param b: 分母
        """
        k = choice(range(2, 5))
        self.tex = choice([str(k) + r"\sqrt{"+ str(a) + "}",\
                                    r"\sqrt{"+ str(a) + "}",\
                           r"\sqrt{4}", r"\sqrt{9}"])

class sjhs(kds):
    def __init__(self,a = 0, b = 0):
        """
        本考点用于生成三角函数
            30    45      60
        sin 1/2   √2/2    √3/2
        cos √3/2  √2/2    1/2
        tan √3/3  1       √3
        :param a: 二次根式下数
        :param b: 分母
        """
        if a == 2:
            self.tex = choice([r"sin 45^{\circ}", r"cos 45^{\circ}"])
        elif a == 3:
            self.tex = choice([r"sin 60^{\circ}", r"cos 30^{\circ}", r"tan 30^{\circ}", r"tan 60^{\circ}"])
        else:
            self.tex = choice([r"sin 30^{\circ}", r"cos 60^{\circ}", r"tan 45^{\circ}"])

class zsfzs(kds):
    def __init__(self, a, b):
        """
        本考点用于生成整数的负指数
        :param a: 二次根式下数
        :param b: 分母
        """
        if b != 0:
            self.tex = f"{b}^"+"{-1}"
        else:
            self.tex = "2^{-1}"

class fsfzs(kds):
    def __init__(self, a, b):
        """
        本考点用于生成整数的负指数
        :param a: 二次根式下数
        :param b: 分母
        """
        possible_list = [r"\frac{1}{2}", r"\frac{1}{3}", r"\frac{1}{4}"]
        if b == 2:
            possible_list.extend([r"\frac{2}{3}", r"\frac{2}{5}"])
        elif b == 3:
            possible_list.extend([r"\frac{3}{2}", r"\frac{3}{4}", r"\frac{3}{5}"])
        elif b == 4:
            possible_list.extend([r"\frac{4}{3}"])
        self.tex = f"({choice(possible_list)})^" + "{-1}"

class gsfzs(kds):
    def __init__(self, a, b):
        """
        本考点用于生成根式的负指数
        :param a: 二次根式下数
        :param b: 分母
        """
        possible_list = [r"\sqrt{\frac{1}{4}}", r"\sqrt{\frac{1}{9}}"]
        if a == 2:
            possible_list.extend([r"\sqrt{\frac{1}{2}}", r"\sqrt{\frac{9}{2}}"])
            if b == 2:
                possible_list.extend([r"\sqrt{2}"])
        elif a == 3:
            possible_list.extend([r"\sqrt{\frac{1}{3}}", r"\sqrt{\frac{4}{3}}"])
            if b == 3:
                possible_list.extend([r"\sqrt{3}"])

        self.tex = f"({choice(possible_list)})" + "^{-1}"

class fzs(kds):
    def __init__(self, a, b):
        """
        本考点用于生成分子为一的负指数
        :param a: 二次根式下数
        :param b: 分母
        """
        posiible_list = ["2", "3", "4"]
        if a == 2:
            posiible_list.append(r"\sqrt{2}")
        elif a == 3:
            posiible_list.append(r"\sqrt{3}")
        self.tex = r"(\frac{1}{" + f"{choice(posiible_list)}" + "})^{-1}"

class jdz(kds):
    def __init__(self, a, b):
        """
        本考点用于生成负数的绝对值
        :param a: 二次根式下数
        :param b: 分母
        """
        posiible_list = [1, 2, 3, 4]
        if a == 2:
            posiible_list.extend([str(k) + r"\sqrt{2}" for k in range(2, 4)])
        elif a == 3:
            posiible_list.append([str(k) + r"\sqrt{3}" for k in range(2, 4)])
        if b == 2:
            posiible_list.extend([r"\frac{1}{2}", r"\frac{3}{2}", r"\frac{5}{2}"])
        elif b == 3:
            posiible_list.extend([r"\frac{1}{3}", r"\frac{2}{3}", r"\frac{4}{3}"])

        self.tex = f"|-{choice(posiible_list)}|"

class cdjdz(kds):
    def __init__(self, a, b):
        """
        本考点用于生成差的绝对值
        :param a: 二次根式下数
        :param b: 分母
        """
        possible_list = []
        if a == 2:
            possible_list.extend([r"2-\sqrt{2}", r"1-\sqrt{2}", r"\sqrt{2}-2", r"\sqrt{2}-1"])
        elif a == 3:
            possible_list.extend([r"1-\sqrt{3}", r"\sqrt{3}-1", r"\sqrt{3}-2", r"2-\sqrt{3}"])
        else:
            possible_list.extend([f"{m}-{abs(m+n+1)}" \
                                  for m in range(-5, 5) \
                                  for n in range(0, 3) \
                                  if not(abs(m+n+1 ==0)  or m == 0)])

        self.tex = f"|{choice(possible_list)}|"

class tsecgs(kds):
    def __init__(self, a, b):
        """
        本考点用于生成特殊的二次根式
        :param a: 二次根式下数
        :param b: 分母
        """
        possible_list = []
        if a != 0:
            possible_list.extend([m**2*a for m in range(2, 4)])
            if a == 2:
                possible_list.extend([r"\frac{1}{2}"])
            elif a == 3:
                possible_list.extend([r"\frac{1}{3}"])
        self.tex = r"\sqrt{" + f"{choice(possible_list)}" + "}"

class gcgs(kds):
    def __init__(self, a, b):
        """
        本考点用于生成高于二次的根式
        :param a: 二次根式下数
        :param b: 分母
        """
        n = choice([4, 3])
        self.tex = r"\sqrt" + f"[{n}]"+ "{" + f"{choice([m**n for m in range(0, 5)])}" + "}"

kd_list = [ocf, lcf, ecgs, sjhs, zsfzs, fsfzs, gsfzs, fzs, jdz, cdjdz, tsecgs, gcgs]

if __name__ == "__main__":
    print(len(kd_list))
    print(choice(kd_list)(3, 3))
    print(gcgs(3,3))
