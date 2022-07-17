import pandas as pd
from pytrends.request import TrendReq
import json


def search(trend):
    file = open('utils/mock.json')
    state_list = json.load(file)
    file.close()

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
                'polygon':state_list[index],
                'popup': f"{index} - {row[trend]}"
                }
            context.append(valor)
    return context