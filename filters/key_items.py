import pandas as pd
import numpy as np
import sqlite3 as sql


# if __name__ == "__main__":
df = pd.read_csv('filters/data/inci_list.csv', index_col='INCI name')

def filter_text(text=None):
    # text = text.replace('\n', ' ').replace('\r', '')
    text = text.lower()
    ingredients = text.split('ingredients:')
    output = {}
    ingredients = ingredients[1]
    ingredients = ingredients.split('\n\n')[0]
    # print(ingredients)
    comps = ingredients.split(',')
    for compound in comps:
        compound = compound[1:]
        pdobj = locate_compound(compound)
        if pdobj is not None:
            output[compound] = pdobj
        else:
            output[compound] = "Not Found"
    return output


def locate_compound(name=None):
    if not name is None:
        name = name.upper()
        try:
            pdobj = df.loc[name]
        except KeyError as e:
            pdobj = None
        return pdobj
    else:
        return None


# # test run
# file1 = open('filters/data/myfile.txt', 'r')
# text = file1.read()
# out = filter_text(text)
# print(out)