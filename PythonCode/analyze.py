import os
from typing import List, Any
import pickle
from cltk.prosody.lat import macronizer, scanner, clausulae_analysis
import csv
import speeches
source_path_caesar = './caesar/'
export_path_caesar = './caesar_pickles/'
table_rows = list()
table_rows_book = list()

export_file = 'Caesar_clausulae.csv'
open(export_file, 'w').close()
standard_clausulae = ["cretic_trochee","cretic_trochee_resolved_a","cretic_trochee_resolved_b","cretic_trochee_resolved_c","double_cretic","molossus_cretic","double_molossus_cretic_resolved_a","double_molossus_cretic_resolved_b","double_molossus_cretic_resolved_c","double_molossus_cretic_resolved_d","double_molossus_cretic_resolved_e","double_molossus_cretic_resolved_f","double_molossus_cretic_resolved_g","double_molossus_cretic_resolved_h","double_trochee","double_trochee_resolved_a","double_trochee_resolved_b","hypodochmiac","hypodochmiac_resolved_a","hypodochmiac_resolved_b","spondaic","heroic"]
column_names = ["Buch", "Satznummer", "Satz", "Klauselname", "Klauselmuster", "KategorieKlausel", "Satzlänge", "Rede", "Artistisch"]

def load_caesar_from_pickles():
    pickle_list: list[Any] = list()
    files = os.listdir(export_path_caesar)
    for file in files:
         pickle_list.append(pickle.load(open(export_path_caesar + file, 'rb')))

    return pickle_list

def analyze_clausulae(books):
    counter_file = 1

    for list_element in books:
        print('Start Round {0}'.format(counter_file))
        cltk_doc = list_element

        scanner_object = scanner.Scansion(punctuation=None, clausula_length=13, elide=True)
        clausel_object = clausulae_analysis.Clausulae()

        table_rows = list()
        if(counter_file == 1): table_rows.append(column_names)

        table_rows_book = list()
        table_rows_book.append(column_names)

        counter = 1


        for sentence in cltk_doc.sentences:
            satz = ''
            clausula_name = ''
            clausula_pattern = ''

            for s in sentence:
                if(s.string==',' or s.string == '.'):
                    element = s.string
                else:
                    element = ' ' + s.string
                satz = satz + element
            satz = satz.lstrip().rstrip()

            sentence_scanned = scanner_object.scan_text(satz.replace(',', ''))
            #sentence_scanned = scanner_object.scan_text(satz)

            clausula_list = clausel_object.clausulae_analysis(sentence_scanned)
            key_list = list()
            val_list = list()
            for clausula in clausula_list:
                key_list.append(list(clausula.keys())[0])
                val_list.append(clausula.get(list(clausula.keys())[0]))
            try:
                position = val_list.index(1)
                clausula_name = key_list[position]
            except:
                clausula_name = ''

            if not sentence_scanned:
                clausula_pattern = ''
            else:
                clausula_pattern = sentence_scanned[0]


            if (satz in speeches.speeches):
                OratioObl = 1
            else:
                OratioObl = 0

            clausula_categorie = 7

            if(clausula_name == 'cretic_trochee'  or
                    clausula_name == 'cretic_trochee_resolved_a' or
                    clausula_name == 'cretic_trochee_resolved_b' or
                    clausula_name == 'cretic_trochee_resolved_c'
            ):
                clausula_categorie = 1
            if(clausula_name == 'double_cretic' or
                    clausula_name == 'molossus_cretic' or
                    clausula_name == 'double_molossus_cretic_resolved_a' or
                    clausula_name == 'double_molossus_cretic_resolved_b' or
                    clausula_name == 'double_molossus_cretic_resolved_c' or
                    clausula_name == 'double_molossus_cretic_resolved_c' or
                    clausula_name == 'double_molossus_cretic_resolved_d' or
                    clausula_name == 'double_molossus_cretic_resolved_e' or
                    clausula_name == 'double_molossus_cretic_resolved_f' or
                    clausula_name == 'double_molossus_cretic_resolved_g' or
                    clausula_name == 'double_molossus_cretic_resolved_h'
            ):
                clausula_categorie = 2

            if(clausula_name == 'double_trochee' or
                    clausula_name == 'double_trochee_resolved_a' or
                    clausula_name == 'double_trochee_resolved_b'
            ):
                clausula_categorie = 3

            if(clausula_name == 'hypodochmiac' or
                    clausula_name == 'hypodochmiac_resolved_a' or
                    clausula_name == 'hypodochmiac_resolved_b'
            ):
                clausula_categorie = 4

            if(clausula_name == 'spondaic'):
                clausula_categorie = 5

            if (clausula_name == 'spondaic'):
                clausula_categorie = 5

            if (clausula_name == 'heroic'):
                clausula_categorie = 6

            if clausula_categorie < 5:
                ARTISTIC = 1
            else:
                ARTISTIC = 0



            table_rows.append([counter_file, counter, satz, clausula_name, clausula_pattern, clausula_categorie, len(sentence.words), OratioObl, ARTISTIC])
            table_rows_book.append([counter_file, counter, satz, clausula_name, clausula_pattern, clausula_categorie, len(sentence.words), OratioObl, ARTISTIC])
            counter = counter + 1



        with open(export_file, 'a', newline='', encoding='UTF8') as csvfile:
            writer = csv.writer(csvfile, dialect='unix')
            writer.writerows(table_rows)
            csvfile.close()


        with open(str(counter_file) + '_' + export_file, 'a', newline='', encoding='UTF8') as csvfile:
            writer = csv.writer(csvfile, dialect='unix')
            writer.writerows(table_rows_book)
            csvfile.close()

        counter_file = counter_file + 1




texts = load_caesar_from_pickles()
analyze_clausulae(texts)