import os
import datetime
import requests
from datetime import date
from urllib.parse import urlparse
import boto3

def build_url():import os

    key = []
    list_state = ['RO',
                  'AC',
                  'AM',
                  'RR',
                  'PA',
                  'AP',
                  'TO',
                  'MA',
                  'PI',
                  'CE',
                  'RN',
                  'PB',
                  'PE',
                  'AL',
                  'SE',
                  'BA',
                  'MG',
                  'ES',
                  'RJ',
                  'SP',
                  'PR',
                  'SC',
                  'RS',
                  'MS',
                  'MT',
                  'GO',
                  'DF',
                  ]

    for year in range(2014, 2022):
        for month in range(1, 13):
            for state in list_state:
                if month <= 9:

                    url.append("http://ftp.dadosabertos.ans.gov.br/FTP/PDA/informacoes_consolidadas_de_beneficiarios/{}0{}/ben{}0{}_{}.zip".format(
                        year, month, year, month, state)
                        )
                    key.append("my_bucket/beneficiaries/{}/ben{}0{}_{}.zip".format(year,year,month,state))


                
                
                
                else:
                    url.append("http://ftp.dadosabertos.ans.gov.br/FTP/PDA/informacoes_consolidadas_de_beneficiarios/{}{}/ben{}{}_{}.zip".format(
                        year, month, year, month, state))

                    key.append("my_bucket/beneficiaries/{}/ben{}{}_{}.zip".format(year,year,month,state))


    return url , key 


if __name__ == '__main__':
    urls , keys = build_url()
    print(keys)
