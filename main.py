# import csv
import pdb

import pandas as pd

import utils


def extract_descriptions(cosmos_file: str, external_descriptions_file: str):
    cosmos = utils.extract_cosmos(cosmos_file)
    external_descriptions = utils.extract_external_descriptions(external_descriptions_file)

    return cosmos.append(external_descriptions, ignore_index=True).drop_duplicates(keep='first')



if __name__=='__main__':
    infomix = utils.extract_infomix('files/infomix.tsv')
    gs1 = utils.extract_gs1('files/gs1.jl')
    cnpj_detail = utils.extract_cnpj_detail('files/cnpjs_receita_federal.jl')
    descriptions = extract_descriptions('files/cosmos.jl', 'files/descricoes_externas.tsv')

    infoprice = pd.merge(infomix, gs1, how='left', left_on='gtin', right_on='gtin')
    infoprice = pd.merge(infoprice, cnpj_detail, how='left', left_on='cnpj', right_on='cnpj')
    infoprice = pd.merge(infoprice, descriptions, how='left', left_on='gtin', right_on='gtin')


    pdb.set_trace()
    # saida: gtin, cnpj, razao social, cidade, estado, descricao, categoria
