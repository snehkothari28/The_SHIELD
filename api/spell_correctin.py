
from symspellpy import SymSpell, Verbosity

import os

def SpellCorrect(strings):
    sym_spell = SymSpell(max_dictionary_edit_distance=1, prefix_length=7)
    # dictionary_path = pkg_resources.resource_filename("symspellpy", "frequency_dictionary_en_82_765.txt")
    # term_index is the column of the term and count_index is the
    # column of the term frequency
    sym_spell.load_dictionary(os.getcwd()+'\\frequency.txt', term_index=0, count_index=1)
    temp = []
    # lookup suggestions for single-word input strings
    for row in strings:
        try:
            suggestions = sym_spell.lookup_compound(row, max_edit_distance=1)
            temp.append(str(suggestions[0]).split(',')[0])
        except:
            temp.append('\n')
    return temp