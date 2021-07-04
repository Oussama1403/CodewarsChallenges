def find_it(seq):
    for n in seq:
        n_of_times = seq.count(n)
        if n_of_times % 2 != 0:
            return n