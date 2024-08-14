from utils.vocab_table import *
from utils.randomize import *
from functools import reduce
import numpy as np
import inspect
import __main__ as main

VOCAB_SETS = {}


def list_current_functions():
    functions = [name for name, obj in inspect.getmembers(main) if inspect.isfunction(obj)]
    return functions


# =================================================
#                    NOUNS
# =================================================

def get_all_noun_case():
    return ['get_all_acusative_pl_noun', 'get_all_acusative_sg_noun','get_all_conjunctive', 'get_all_dative_pl_noun',
            'get_all_dative_sg_noun', 'get_all_genitiv_pl_noun', 'get_all_genitiv_sg_noun',
            'get_all_instrumental_pl_noun', 'get_all_instrumental_sg_sg_noun', 'get_all_local_pl_noun', 'get_all_local_sg_noun']

def get_all_nouns():
    if "all_nouns" not in VOCAB_SETS.keys():
        VOCAB_SETS["all_nouns"] = get_all("kategoria","pods")
    return VOCAB_SETS["all_nouns"] 

def get_all_genitiv_sg_noun(vocab):
        if "all_genitiv_sg_noun" not in VOCAB_SETS.keys():
            VOCAB_SETS["all_genitiv_sg_noun"] = get_specific_column("genitív_sg", vocab)
        return VOCAB_SETS["all_genitiv_sg_noun"] 

def get_all_dative_sg_noun(vocab):
        if "all_genitiv_sg_noun" not in VOCAB_SETS.keys():
            VOCAB_SETS["all_genitiv_sg_noun"] = get_specific_column('dative_sg', vocab)
        return VOCAB_SETS["all_genitiv_sg_noun"] 

def get_all_local_sg_noun(vocab):
        if "all_genitiv_sg_noun" not in VOCAB_SETS.keys():
            VOCAB_SETS["all_genitiv_sg_noun"] = get_specific_column('local_sg', vocab)
        return VOCAB_SETS["all_genitiv_sg_noun"] 

def get_all_acusative_sg_noun(vocab):
        if "all_genitiv_sg_noun" not in VOCAB_SETS.keys():
            VOCAB_SETS["all_genitiv_sg_noun"] = get_specific_column('acusative_sg', vocab)
        return VOCAB_SETS["all_genitiv_sg_noun"] 

def get_all_instrumental_sg_sg_noun(vocab):
        if "all_genitiv_sg_noun" not in VOCAB_SETS.keys():
            VOCAB_SETS["all_genitiv_sg_noun"] = get_specific_column('instrumental_sg', vocab)
        return VOCAB_SETS["all_genitiv_sg_noun"] 


def get_all_genitiv_pl_noun(vocab):
        if "all_genitiv_pl_noun" not in VOCAB_SETS.keys():
            VOCAB_SETS["all_genitiv_pl_noun"] = get_specific_column("genitív_pl", vocab)
        return VOCAB_SETS["all_genitiv_pl_noun"] 

def get_all_dative_pl_noun(vocab):
        if "all_genitiv_pl_noun" not in VOCAB_SETS.keys():
            VOCAB_SETS["all_genitiv_pl_noun"] = get_specific_column('dative_pl', vocab)
        return VOCAB_SETS["all_genitiv_pl_noun"] 

def get_all_local_pl_noun(vocab):
        if "all_genitiv_pl_noun" not in VOCAB_SETS.keys():
            VOCAB_SETS["all_genitiv_pl_noun"] = get_specific_column('local_pl', vocab)
        return VOCAB_SETS["all_genitiv_pl_noun"] 

def get_all_acusative_pl_noun(vocab):
        if "all_genitiv_pl_noun" not in VOCAB_SETS.keys():
            VOCAB_SETS["all_genitiv_pl_noun"] = get_specific_column('acusative_pl', vocab)
        return VOCAB_SETS["all_genitiv_pl_noun"] 

def get_all_instrumental_pl_noun(vocab):
        if "all_genitiv_pl_noun" not in VOCAB_SETS.keys():
            VOCAB_SETS["all_genitiv_pl_noun"] = get_specific_column('instrumental_pl', vocab)
        return VOCAB_SETS["all_genitiv_pl_noun"] 



# =================================================
#                    NOUNS
# =================================================