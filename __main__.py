# from parse_notebook import *
# from process_abf import *
# from process_cells import *
import csv
import os
import sys
sys.path.append('/Users/mingxiaowei/Desktop/lab/HCN_scripts')
from process_cells import process_cell
from parse_notebook import parse_notebook
exp_folder = '20220729 HCN Channel Investigation RD1'

def main():
    # parse experiment info
    exp = parse_notebook(exp_folder)
    mouse = exp.mouse
    HCN_voltage = list(range(-60, -121, -10))

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
        writer.writerow('')
        
        # write cell info
        for i in range(1, len(exp.cells) + 1):
            writer.writerow([f'Cell_{i}'])
            curr_cell = process_cell(i, exp, exp_folder)
            writer.writerow(['Voltage Step (mV)'] + HCN_voltage)
            writer.writerow(['HCN Current (pA)'] + curr_cell.HCN_rec.delta_lst)
            writer.writerow('')


        

if __name__ == '__main__':
    main()
