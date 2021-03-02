import pandas as pd

import utils


def extract_descriptions(cosmos_file: str, external_descriptions_file: str):
    cosmos = utils.extract_cosmos(cosmos_file)
    external_descriptions = utils.extract_external_descriptions(external_descriptions_file)

    return cosmos.append(external_descriptions, ignore_index=True).drop_duplicates(keep='first')


def extract():
    infomix = utils.extract_infomix('inputs/infomix.tsv')
    gs1 = utils.extract_gs1('inputs/gs1.jl')
    cnpjs = utils.extract_cnpj_detail('inputs/cnpjs_receita_federal.jl')
    descriptions = extract_descriptions('inputs/cosmos.jl', 'inputs/descricoes_externas.tsv')

    return infomix, gs1, cnpjs, descriptions


def treat(infomix, gs1, cnpjs, descriptions):
    infoprice = pd.merge(infomix, gs1, how='inner', left_on='gtin', right_on='gtin')
    infoprice = pd.merge(infoprice, cnpjs, how='left', left_on='cnpj', right_on='cnpj')
    infoprice = pd.merge(infoprice, descriptions, how='left', left_on='gtin', right_on='gtin')

    return infoprice


def load(df, file: str):
    df.to_csv(file, header='True', index=False)

    return None


if __name__ == '__main__':

    infomix, gs1, cnpjs, descriptions = extract()
    infoprice = treat(infomix, gs1, cnpjs, descriptions)

    infoprice[['gtin', 'cnpj', 'name', 'city', 'state', 'description', 'category']] \
        .set_axis(['GTIN', 'CNPJ', 'RAZÃO SOCIAL', 'CIDADE', 'ESTADO', 'DESCRIÇÃO', 'CATEGORIA'], axis=1) \
        .to_csv("outputs/infoprice.csv", header=True, index=False)
