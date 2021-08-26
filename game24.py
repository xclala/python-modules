def game24(n1:int=0, n2:int=0, n3:int=0, n4:int=0):
    """author:Dong Xing
    python_version:>=python3.6
    Calculate game24.
    2020.8.3 Monday
    Instead of multiplying and dividing and then adding and subtracting, do it from left to right!
    """
    from itertools import permutations, product
    from warnings import warn
    for a, b, c, d in permutations((n1, n2, n3, n4)):
        for o1, o2, o3 in product(['+', '-', '*', '/'], repeat=3):
            cases = list()
            cases.append(f"{a}{o1}{b}{o2}{c}{o3}{d}")
            cases.append(f"({a}{o1}{b}){o2}{c}{o3}{d}")
            cases.append(f"{a}{o1}{b}{o2}({c}{o3}{d})")
            cases.append(f"{a}{o1}({b}{o2}{c}){o3}{d}")
            cases.append(f"({a}{o1}{b}){o2}({c}{o3}{d})")
            cases.append(f"({a}{o1}{b}{o2}{c}){o3}{d}")
            cases.append(f"(({a}{o1}{b}){o2}{c}){o3}{d}")
            cases.append(f"({a}{o1}({b}{o2}{c})){o3}{d}")
            cases.append(f"{a}{o1}({b}{o2}{c}{o3}{d})")
            cases.append(f"{a}{o1}(({b}{o2}{c}){o3}{d})")
            cases.append(f"{a}{o1}({b}{o2}({c}{o3}{d}))")
            cases.append(f"({a}{o1}{b}{o2}{c}){o3}{d}")
            for expression in cases:
                try:
                    if eval(expression)==24:
                        return expression
                except:
                    pass
    print('No solution.') 


