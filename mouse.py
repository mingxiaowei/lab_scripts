from experiment import *

class Mouse: 

    def __init__(self, genotype, gender, bday_str, exp=None):
        self.genotype = genotype 
        self.gender = gender 
        self.set_birth_day(bday_str)
        self.experiment = exp 
        self.age = -1
        if self.experiment:
            self.experiment.set_mouse(self)
            self.age = (self.experiment.date - self.birth_date).days

    def __repr__(self):
        return f'Mouse({self.genotype}, {self.gender}, {self.birth_date}, {self.experiment})'
    
    def set_birth_day(self, bday_str):
        date_lst = list(map(int, bday_str.split('/')))
        if date_lst[2] < 2000: # handle shorthand notation for year
            date_lst[2] += 2000
        self.birth_date = date(date_lst[2], date_lst[0], date_lst[1])