from datetime import date

class Cell:
    
    def __init__(self, cm, rm, ra, tau, hold, depth):
        self.cm = cm # pF
        self.rm = rm # MOhms
        self.ra = ra # MOhms
        self.tau = tau # ms
        self.hold = hold # pA 
        self.depth = depth # um
        self.HCN_rec = None # HCNEvent object
        self.id = None # format: YYYYMMDD_Cell#
        self.experiment = None
    
    def __repr__(self):
        return f'Cell({self.cm}, {self.rm}, {self.ra}, {self.tau}, {self.hold}, {self.depth})'
    
    def __str__(self):
        cell_str = self.id
        cell_str += f'\nMembrane capacitance = {self.cm} pF'
        cell_str += f'\nMembrane resistance = {self.rm} MOhms'
        cell_str += f'\nAccess resistance = {self.ra} MOhms'
        cell_str += f'\nTime constant = {self.tau} ms'
        cell_str += f'\nHolding current = {self.hold} pA'
        cell_str += f'\nSoma to dendrite = {self.depth} μm'
        return cell_str + '\n'
    
    def info_lst_csv(self):
        info_lst = []
        info_lst.append(['Membrane capacitance (pF)', self.cm])
        info_lst.append(['Membrane resistance (MOhms)', self.rm])
        info_lst.append(['Access resistance (MOhms)', self.ra])
        info_lst.append(['Time constant (ms)', self.tau])
        info_lst.append(['Holding current (pA)', self.hold])
        info_lst.append(['Soma to dendrite (μm)', self.depth])
        return info_lst
    
    def set_experiment(self, exp, cnt):
        self.experiment = exp
        self.id = f"{exp.date.strftime('%Y%m%d')}_Cell{cnt}"
        exp.cells.append(self)
    
    def set_HCN_rec(self, rec):
        self.HCN_rec = rec
        
