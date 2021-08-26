def all_random(fstnum,fennum,sstnum,sennum):
    from random import choice,randint
    _ = str(randint(fstnum, fennum)) + \
        choice(['+', '-', '*', '/', '//', '%'])+str(randint(sstnum, sennum))
    print(_)
    return eval(_)
