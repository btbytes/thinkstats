#!/usr/bin/env python
from __future__ import print_function
import sys
import survey

def num_pregs(data_dir="../data"):
    table = survey.Pregnancies()
    table.ReadRecords(data_dir)
    print('Number of Pregnancies: ', len(table.records))

def live_births(data_dir="../data"):
    table = survey.Pregnancies()
    table.ReadRecords(data_dir)
    lb = [r for r in table.records if r.outcome == 1]
    print('Number of live births: ', len(lb))

def main(name, data_dir="../data"):
    num_pregs()
    live_births()
    
if __name__ == '__main__':
    main(*sys.argv)
