from datetime import date
from cell import *

class Experiment:

    def __init__(self, date_str, title):
        self.date = date(int(date_str[:4]), int(date_str[4:6]), int(date_str[-2:])) # date_str: YYYYMMDD
        self.title = title 
        self.cells = [] # a list of Cell objects 
        self.blockers = [] 
        self.internal_soln = None
        self.mouse = None 
    
    def __repr__(self):
        return f'Experiment({self.date}, {self.title})'

    def set_mouse(self, mouse):
        self.mouse = mouse
    
    def set_blockers(self, blockers):
        self.blockers = blockers
    
    def set_internal_soln(self, soln):
        self.internal_soln = soln
    
    def print_cell_stats(self):
        for c in self.cells:
            print(c)

