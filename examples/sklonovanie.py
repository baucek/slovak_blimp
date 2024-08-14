from utils.randomize import choice
from utils.vocab_table import *
from utils.vocab_dynamics import *
from utils import data_generator


class CSCGenerator(data_generator.BenchmarkGenerator):
    def __init__(self):
        super().__init__(field="Sklonovanie",
                         linguistics="island",
                         uid="Sulad_pods_prid",
                         simple_lm_method=True,
                         one_prefix_method=False,
                         two_prefix_method=False,
                         lexically_identical=True)



    def sample(self):
        # What did      John read  before filing the book?
        # Wh   Aux_mat  Subj V_mat ADV    V_emb  Obj
        # What did      John read  the book before filing?
        # Wh   Aux_mat  Subj V_mat Obj      ADV    V_emb
        gr_cat=choice_gr(get_all_noun_case())

        V_mat = choice(gr_cat(get_all('hypermnym', '1', get_all_nouns())))









        # Subj = N_to_DP_mutate(choice(get_matches_of(V_mat, "arg_1", get_all_nouns())))
        # Aux_mat = return_aux(V_mat, Subj, allow_negated=False)
        # Obj = N_to_DP_mutate(choice(get_matches_of(V_mat, "arg_2", get_all_nouns())))
        # V_emb = choice(get_matched_by(Obj, "arg_2", get_matched_by(Subj, "arg_1", self.all_ing_transitives)))
        # Wh = choice(get_matched_by(Obj, "arg_1", get_all_wh_words()))
        # Adv = choice(self.adverbs)

        data = {
            "sentence_good": "%s." % (V_mat),
            "sentence_bad": "%s." % (V_mat)
        }
        return data, data["sentence_good"]

generator = CSCGenerator()
# rel_output_path=
generator.generate_paradigm(absolute_path="C:\\Users\\Dell\\Desktop\\Diplomovka\\Blimp\\data_generation_svk\\examples\\%s.jsonl" % generator.uid)



# # all names function
# functions_list = list_current_functions()
# print(functions_list)
