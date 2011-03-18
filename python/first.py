#!/usr/bin/env python

import sys
import survey

def main(name, data_dir="../data"):
    table = survey.Pregnancies()
    table.ReadRecords(data_dir)
    print 'Number of Pregnencies: ', len(table.records)

if __name__ == '__main__':
    main(*sys.argv)
    
