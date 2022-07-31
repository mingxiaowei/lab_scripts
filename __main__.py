# from parse_notebook import *
# from process_abf import *
# from process_cells import *
import csv
import os
import sys
sys.path.append('/Users/mingxiaowei/Desktop/lab/HCN_scripts')
# print(sys.path)

from parse_notebook import parse_notebook

def main():
    # parse experiment info
    exp = parse_notebook()
    mouse = exp.mouse

    # determine output file name
    dir_lst = os.listdir(os.path.dirname(__file__))
    output_file = 'output.csv'
    cnt = 1
    while output_file in dir_lst:
        output_file = f'output_{cnt}.csv'
        cnt += 1
    with open(output_file, 'w') as file:
        writer = csv.writer(file)

        # write experiment info
        exp_info_lst = [[exp.date, exp.title], '', ['Blockers'] + exp.blockers, '', ['Internal Solution', exp.internal_soln], '']
        mouse_info_lst = ['Mouse Info', ['Genotype'] + mouse.genotype, ['Gender', mouse.gender], ['DOB', mouse.birth_date], ['Age (days)', mouse.age]]
        metadata_lst = list(map(lambda x: x if isinstance(x, list) else [x], exp_info_lst + mouse_info_lst))
        for i in metadata_lst:
            writer.writerow(i)
        
        # write cell info
        
        

if __name__ == '__main__':
    main()
