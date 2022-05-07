import os
from cltk import NLP
import pickle
import normalizer

source_path_caesar = './caesar/'
export_path_caesar = './caesar_pickles/'
source_path_cicero = './cicero/'
export_path_cicero = './cicero_pickles/'

def pickle_ceasar():
    cltk_nlp = NLP(language="lat")
    cltk_nlp.pipeline.processes.pop(-1)
    files = os.listdir(source_path_caesar)

    for f in files:
        if(f[0] != '_'):
            with open(source_path_caesar + f, 'r', encoding='UTF-8') as stream:
                text = stream.read()

            normi = normalizer.Normalizer()
            normed_text = normi.normalize(text)
            cltk_doc = cltk_nlp.analyze(normed_text)
            pickle.dump(cltk_doc, open('{0}{1}.pkl'.format(export_path_caesar, f), 'wb'))

pickle_ceasar()