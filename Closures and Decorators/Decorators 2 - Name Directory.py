"""Decorators 2 - Name Directory.py"""

def formatter(func):
    """wrapper function"""
    def sorter(ppl):
        """alters format of ppl lists and then sorts then based on age"""
        new_ppl = []
        for person in ppl:
            new_ppl.append([" ".join(person[:2]), int(person[2]), person[3]])
        ppl = sorted(new_ppl, key = lambda x: x[1])
        ppl = [[x[0], x[2]] for x in ppl]
        return func(ppl)
    return sorter

@formatter
def namer(ppl):
    """adds prefix to front of name based on sex"""
    return [(lambda x: "Ms. " + x[0] if x[1] == "F" else "Mr. " + x[0])(x) for x in ppl]

PPL = [input().split() for i in range(int(input()))]
print("\n".join(namer(PPL)))
