import re
import numpy as np
# from utils.data_type import *
from data_type import *

import os
import glob

list_type=[data_type_pods, data_type_prid]

def load_and_expand(file_path,data_type):
    data = np.genfromtxt(file_path, dtype=data_type, delimiter=",", names=True, encoding="utf8")
    return data

directory_path = f"C:/Users/Dell/Desktop/Diplomovka/Blimp/data_generation_svk/examples/utils/prompty/Testing"

file_paths = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if f.endswith('.txt')]


full_data =np.empty()
for number,file_path in enumerate(file_paths):
    data = load_and_expand(file_path,list_type[number])

    full_data=np.concatenate(full_data,data)
# print(final_data)




















































current_directory = os.path.dirname(os.path.abspath(__file__))

vocab = np.genfromtxt(f"{current_directory}/prompty/podstatne_meno.txt", dtype=data_type_pods,delimiter=",", names=True, encoding="utf8")
print('')


def get_all(label, value, table=vocab):
    """
    :param label: string. field name.
    :param value: string. label.
    :param table: ndarray of vocab items.
    :return: table restricted to all entries with "value" in field "label"
    """
    # TODO: this should not be based on string equality, but disjunction matching
    # return np.array(list(filter(lambda x: condition_is_match_disj(value, x[label]), table)), dtype=data_type)
    return np.array(list(filter(lambda x: x[label] == value, table)), dtype=table.dtype)


def get_all_conjunctive(labels_values, table=vocab):
    """
    :param labels_values: list of (l,v) pairs: [(l1, v1), (l2, v2), (l3, v3)]
    :return: vocab items with the given value for each label
    """
    to_return = table
    for label, value in labels_values:
        to_return = np.array(list(filter(lambda x: x[label] == value, to_return)), dtype=table.dtype)
    return to_return

def get_specific_column(label, table=vocab):
    """
    :param specific column:"genitív_sg" str; vocab: numpy of words 
    :return: list of strings
    """
    gen_list=table[label].tolist()
    return list(filter(None, gen_list))

def get_concise_table(label, table=vocab): 
    vocab[:, label]
    return vocab
#     return 



