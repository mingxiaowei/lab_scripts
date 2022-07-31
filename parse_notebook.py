from striprtf.striprtf import rtf_to_text
import re
import os
from cell import *
from experiment import *
from mouse import Mouse

current_dir = os.path.dirname(__file__)
relative_path = "../lab notebook (1).rtf" # relative path to this script. *** CHANGE FOR EACH EXPERIMENT ***
lines = [] # a list of all lines in lab notebook
experiment = None # replaced with the Experiment object later 

def read_lines(): 
    with open(os.path.join(current_dir, relative_path)) as infile:
        for line in infile:
            line = rtf_to_text(line)
            if len(line) > 0 and not re.fullmatch(r'\s', line): # remove blank lines
                line = re.sub('\n', '', line) # remove new lines characters
                lines.append(line)

def parse_metadata(): 
    global experiment

    # parse experiment date and title 
    experiment = Experiment(lines[0][:8], lines[0][9:])

    # parse mouse info
    mouse_info = lines[2].split(', ')
    genotype_lst = mouse_info[:3]
    gender = mouse_info[3]
    if re.search(r'\b[Mm]ale\b|\b[Ff]emale\b', genotype_lst[-1]):
        gender = re.findall(r'\b[Mm]ale\b|\b[Ff]emale\b', genotype_lst[-1])[0]
        genotype_lst[-1] = genotype_lst[-1].replace(gender, '')
        # genotype_lst[-1] = re.sub(r'\s*', '', genotype_lst[-1])
    bday_str = mouse_info[-1].split(' ')[1]
    mouse = Mouse(genotype_lst, gender, bday_str, experiment) # this will mutate the experiment object 

    # parse blockers
    blockers = lines[3][len('Blockers: '):].split(', ') # remove 'Blockers: '
    # remove blank/empty strings from list
    blockers = list(filter(lambda s: s and not re.fullmatch(r'\W+', s), blockers))
    # handle MFa formatting
    if '. +MFa' in blockers[-1]:
        temp = blockers[-1].split('. ')
        blockers[-1] = temp[0]
        blockers.append(temp[1])
        if blockers[-1][-1] == ',':
            blockers[-1] = blockers[-1][:-1]
        if blockers[-1][0] == '+':
            blockers[-1] = blockers[-1][1:]
    experiment.set_blockers(blockers)

    # parse internal solution
    experiment.set_internal_soln(lines[4][len('Internal Soln: '):])

def parse_cells(): 
    # parse cells 
    cell_cnt = 0
    line_idx = 0
    while line_idx < len(lines):
        # TODO: parse notes/identity for the cell
        if re.match(r'-+\s*', lines[line_idx]): # start new cell -----
            cell_cnt += 1 
            # parse cell depth 
            contain_depth = False 
            while not contain_depth and line_idx + 1 < len(lines):
                line_idx += 1 
                contain_depth = lines[line_idx].startswith('soma to')
                if 'Membrane capacitance' in lines[line_idx]:
                    break
            if contain_depth:
                cell_depth = float(re.findall(r'=\s*(\d+\.?\d*)\b', lines[line_idx])[0])
            else:
                cell_depth = 0
            # parse other cell stats 
            contain_cm = False 
            while not contain_cm and line_idx + 1 < len(lines):
                line_idx += 1
                contain_cm = 'Membrane capacitance' in lines[line_idx]
            if line_idx + 1 >= len(lines):
                break
            cell_cm = float(re.findall(r'=\s*(\d+\.?\d*)\b', lines[line_idx])[0])
            line_idx += 1 
            cell_rm = float(re.findall(r'=\s*(\d+\.?\d*)\b', lines[line_idx])[0])
            line_idx += 1
            cell_ra = float(re.findall(r'=\s*(\d+\.?\d*)\b', lines[line_idx])[0])
            line_idx += 1 
            cell_tau = float(re.findall(r'=\s*(\d+\.?\d*)\b', lines[line_idx])[0])
            if cell_tau > 100: # when unit is in us
                cell_tau /= 1000
            line_idx += 1 
            cell_hold = float(re.findall(r'=\s*(-\d+\.?\d*)\b', lines[line_idx])[0])
            line_idx += 1
            new_cell = Cell(cell_cm, cell_rm, cell_ra, cell_tau, cell_hold, cell_depth)
            new_cell.set_experiment(experiment, cell_cnt)
            # TODO: only parse the last set of stats if multiple exist for one cell - currently only parse the first set 
        line_idx += 1

def parse_notebook():
    global experiment 
    read_lines()
    parse_metadata()
    parse_cells()
    return experiment        

