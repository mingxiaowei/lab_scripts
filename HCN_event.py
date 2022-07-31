class HCNEvent:
    
    def __init__(self, start_lst, end_lst):
        self.start_lst = start_lst
        self.end_lst = end_lst
        self.delta_lst = [s - e for s, e in zip(start_lst, end_lst)]