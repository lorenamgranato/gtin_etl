import json_lines
import pandas as pd


def extract_cnpj_detail(file: str):
    """
    Reads a file from Receita Federal and returns a DataFrame with CNPJ and "razao social".
    Parameters:
    - file: .js file with path to be read.
    """

    cnpj_list = []
    with open(file, 'rb') as f:
        for item in json_lines.reader(f):
            try:
                cnpj = item['cnpj']
                name = item['response']['nome']
                cnpj_list.append({'cnpj': cnpj, 'name': name})
            except:
                pass
    return pd.DataFrame(data=cnpj_list)


def extract_cosmos(file: str):
    """
    Reads a Cosmos file and returns a DataFrame with GTIN and description.
    Parameters:
    - file: .js file with path to be read.
    """
    cosmos_list = []

    with open(file, 'rb') as f:
        for item in json_lines.reader(f):
            try:
                cosmos_list.append({'gtin': item['gtin'], 'description': item['response']['description']})
            except:
                pass

    return pd.DataFrame(data=cosmos_list, dtype='str')


def extract_external_descriptions(file: str):
    """
    Reads a external description files and returns a DataFrame containing GTIN and description.
    Parameters:
    - file: .csv file with path to be read.
    """

    return pd.read_csv(file, sep='\t', usecols=['gtin', 'description'], dtype='str')


def extract_gs1(file: str):
    """
    Reads a GS1 file and returns a DataFrame containing GTIN, city and state for valid responses.
    Parameters:
    - file: .js file with path to be read.
    """
    gs1_list = []
    with open(file, 'rb') as f:
        for item in json_lines.reader(f):
            if item['response']['status'] == 'OK':
                try:
                    gtin = item['gtin']
                    city = item['response']['gepirParty']['partyDataLine']['address']['city']
                    state = item['response']['gepirParty']['partyDataLine']['address']['state']

                    gs1_list.append({'gtin': gtin, 'city': city, 'state': state})
                except:
                    pass
    
    return pd.DataFrame(data=gs1_list)


def extract_infomix(file: str):
    """
    Reads a infomix base and returns it as a DataFrame.
    Parameters:
    - file: .csv file with path to be read.
    """
    return pd.read_csv(file, sep='\t', dtype='str')