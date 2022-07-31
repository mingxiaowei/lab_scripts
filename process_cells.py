# from process_abf import *
import os
current_dir = os.path.dirname(__file__)
relative_path = '../'
dir_lst = os.listdir(os.path.join(current_dir, relative_path))
print(dir_lst)