from process_abf import *
from cell import *
from experiment import *
import os

current_dir = os.path.dirname(__file__)
relative_path = '../'
# dir_lst = os.listdir(os.path.join(current_dir, relative_path))

def process_cell(i, exp, exp_title):
    cell_str = f'Cell{i}'
    new_relative_path = f"{relative_path}{exp_title}/{cell_str}"
    dir_lst = os.listdir(os.path.join(current_dir, new_relative_path))
    for dir in dir_lst:
        # TODO: handle the case where no HCN file is found
        if cell_str in dir and 'HCN' in dir:
            abf_name = f'{new_relative_path}/{dir}'
            HCN_rec = read_abf(abf_name)
            exp.cells[i - 1].set_HCN_rec(HCN_rec)
    return exp.cells[i - 1]