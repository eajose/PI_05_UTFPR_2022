import pandas as pd
from pytrends.request import TrendReq


def search(trend):
    state_list = {
        "Acre": [ -8.77, -70.55], 
        "Alagoas": [ -9.71, -35.73], 
        "Amazonas": [ -3.07, -61.66], 
        "Amapá": [  1.41, -51.77], 
        "Bahia": [-12.96, -38.51], 
        "Ceará": [ -3.71, -38.54], 
        "Distrito Federal": [-15.83, -47.86], 
        "Espírito Santo": [-19.19, -40.34], 
        "Goiás": [-16.64, -49.31], 
        "Maranhão": [ -2.55, -44.30], 
        "Mato Grosso": [-12.64, -55.42], 
        "Mato Grosso do Sul": [-20.51, -54.54], 
        "Minas Gerais": [-18.10, -44.38], 
        "Paraná": [ -5.53, -52.29], 
        "Paraíba": [ -7.06, -35.55], 
        "Pará": [-24.89, -51.55], 
        "Pernambuco": [ -8.28, -35.07], 
        "Piauí": [ -8.28, -43.68], 
        "Rio Grande do Norte": [-22.84, -43.15], 
        "Rio Grande do Sul": [ -5.22, -36.52], 
        "Rio de Janeiro": [-11.22, -62.80], 
        "Rondônia": [-30.01, -51.22], 
        "Roraima": [  1.89, -61.22], 
        "Santa Catarina": [-27.33, -49.44], 
        "Sergipe": [-10.90, -37.07], 
        "São Paulo": [-23.55, -46.64], 
        "Tocantins": [-10.25, -48.25]
    }

    pytrends = TrendReq(hl='pt-BR', tz=360)
    kw_list=[trend]
    pytrends.build_payload(kw_list, geo = 'BR')

    print('\nPesquisando...\n\n')
    df = pytrends.interest_by_region(
        resolution='COUNTRY', 
        inc_low_vol=True, 
        inc_geo_code=False
        )
    
    context = []
    
    for index, row in df.iterrows():
        if row[trend] > 0:
            valor = {
                'lat':state_list[index][0],
                'lon':state_list[index][1],
                'popup': f"{index} - {row[trend]}"
                }
            context.append(valor)
    return context