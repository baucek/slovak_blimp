# from utils.conjugate import *
# from utils.string_utils import string_beautify
# from utils.exceptions import *
# from random import choice
from functools import reduce
import numpy as np
from utils.randomize import choice
import jsonlines
import logging
import datetime
import traceback
import os 

class Generator:
    """
    "Abstract" Class that is instantiated by individual data generation scripts
    """
    def __init__(self):
        self.data_fields = None
        return

    def sample(self):
        """
        samples a single minimal pair/set of a paradigm
        :return: the dictionary containing the data, and a representative sentence to avoid generating duplicates
        """
        data = None
        track_sentence = None
        return data, track_sentence

    def make_metadata_dict(self):
        return {}

    def make_logger(self, metadata):
        """
        creates a logger for the generation project
        :param metadata: metadata dict for the generation project
        :return: None
        """
        project_root = "/".join(os.path.join(os.path.dirname(os.path.abspath(__file__))).split("/")[:-1])
        log_dir = os.path.join(project_root, "logs")
        log_file = 'generation-%s-%s.log' % (metadata["UID"], str(datetime.datetime.now()))
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
        logging.basicConfig(filename=os.path.join(log_dir, log_file), level=logging.DEBUG)

    def log_exception(self, e):
        logging.debug(self.get_stack_trace(e) + "\n")

    def get_stack_trace(self, e):
        return "".join(traceback.format_tb(e.__traceback__)) + str(e)

    def generate_paradigm(self, number_to_generate=1000, rel_output_path=None, absolute_path=None):
        """
        Contains the main loop for generating a full dataset for a given paradigm.
        Also contains exception handling: some exceptions are tolerated because sometimes no matching arguments can be found,
        but if at least 10% of cases have an exception, it terminates since this is probably an issue in the code, and
        it could cause an infinite loop otherwise.
        :param number_to_generate: number of minimal pairs/sets to generate
        :param rel_output_path: relative path of output file
        :param absolute_path: absolute path of output file
        :return: None
        """
        if rel_output_path is not None:
            project_root = 'C:\\Users\\Dell\\Desktop\\Diplomovka\\Blimp\\data_generation_svk\\examples'
            output = open(os.path.join(project_root, rel_output_path), "w")
        elif absolute_path is not None:
            output = open(absolute_path, "w")
        else:
            raise Exception("You need to give an output path")
        past_sentences = set()
        generated_data = []
        pairID = 0
        error_counter = 0
        constant_data = self.make_metadata_dict()
        print("Generating data for " + constant_data["UID"])
        # self.make_logger(constant_data)
        output_writer = jsonlines.Writer(output, flush=True)
        while len(past_sentences) < number_to_generate:
            try:
                new_data, track_sentence = self.sample()
                if track_sentence not in past_sentences:
                    past_sentences.add(track_sentence)
                    for field in self.data_fields:
                        if field in new_data:
                            # new_data[field] = string_beautify(new_data[field])
                            new_data.update(constant_data)
                    new_data["pairID"] = str(pairID)
                    pairID += 1
                    if pairID % 100 == 0:
                        print("%d sentences generated" % pairID)
                    output_writer.write(new_data)
            except Exception as e:
                self.log_exception(e)
                print(self.get_stack_trace(e))
                error_counter += 1
                if error_counter > number_to_generate // 5:
                    pass
                    # raise Exception("Over 20\% of samples result in errors. You should fix this.")
        jsonlines.Writer(output).write_all(generated_data)



class BenchmarkGenerator(Generator):
    """
    Data generator for BLiMP.
    """
    def __init__(self,
                 field: str,
                 linguistics: str,
                 uid: str,
                 simple_lm_method: bool,
                 one_prefix_method: bool,
                 two_prefix_method: bool,
                 lexically_identical: bool,
                 category: str=None):
        super().__init__()
        self.field = field
        self.linguistics = linguistics
        self.uid = uid
        self.simple_lm_method = simple_lm_method
        self.one_prefix_method = one_prefix_method
        self.two_prefix_method = two_prefix_method
        self.lexically_identical = lexically_identical
        self.data_fields = ["sentence_good", "sentence_bad", "one_prefix_prefix", "two_prefix_prefix_good", "two_prefix_prefix_bad"]

    def make_metadata_dict(self):
        """
        (non token-specific metadata is in class fields, e.g. self.field=syntax)
        :param extra_metadata: token-specific metadata, e.g. one_prefix_word_1="the" 
        :return: join metadata
        """
        metadata = {
            "field": self.field,
            "linguistics_term": self.linguistics,
            "UID": self.uid,
            "simple_LM_method": self.simple_lm_method,
            "one_prefix_method": self.one_prefix_method,
            "two_prefix_method": self.two_prefix_method,
            "lexically_identical": self.lexically_identical
        }
        return metadata