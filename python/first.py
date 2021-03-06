#!/usr/bin/env python3.2

import sys
import functools
import survey


@functools.lru_cache(maxsize=10)
def num_pregs(data_dir="../data"):
    '''
    >>> print(num_pregs())
    13593
    '''
    table = survey.Pregnancies()
    table.ReadRecords(data_dir)
    return len(table.records)


@functools.lru_cache(maxsize=10)
def live_births(data_dir="../data"):
    '''
    http://nsfg.icpsr.umich.edu/cocoon/WebDocs/NSFG/public/preg--303-1158-var
    >>> print(len(live_births()))
    9148
    '''
    table = survey.Pregnancies()
    table.ReadRecords(data_dir)
    lb = [r for r in table.records if r.outcome == 1]
    return lb


@functools.lru_cache(maxsize=10)
def first_babies():
    '''
    how many first babies?

    >>> print(len(first_babies()))
    4413
    '''
    return [fb for fb in live_births() if fb.birthord == 1]


@functools.lru_cache(maxsize=10)
def other_babies():
    '''
    non-first-borns
    http://nsfg.icpsr.umich.edu/cocoon/WebDocs/NSFG/public/preg--303-1159-var
    >>> print(len(other_babies()) == (13593-(4445+len(first_babies()))))
    True
    '''
    return [b for b in live_births() if b.birthord in range(2, 11)]


def avg_pregnancy_length(group):
    vals = [b.prglength for b in group]
    return float(sum(vals)) / len(vals)


def main(name, data_dir="../data"):
    np = num_pregs()
    print("CHAPTER ONE\n")
    print('Number of Pregnancies: ', np)
    lb = live_births()
    print('Number of live births: ', len(lb))
    ob = other_babies()
    print('Number of non-first-borns: ', len(ob))
    apl_fb = avg_pregnancy_length(first_babies())
    print('Average Preg. Length for first babies: ', apl_fb)
    apl_nfb = avg_pregnancy_length(other_babies())
    print('Average Preg. Length for non-first babies: ', apl_nfb)
    print('Diff in gestation period bn first and non-first-borns: %.2f hours' \
          % (24 * 7 * (0.6 - 0.52), ))

if __name__ == '__main__':
    main(*sys.argv)
    import doctest
    doctest.testmod()
