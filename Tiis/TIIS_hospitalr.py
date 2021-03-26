import numpy as np
import datetime
import requests
import os
from datetime import date
from urllib.parse import urlparse
import boto3

def get_url_list():
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
    period = range( 2015 , 2022 )
    primary_url = "http://ftp.dadosabertos.ans.gov.br/FTP/PDA/TISS/HOSPITALAR/{}/{}.zip"
    list_url = []
    key_path = []
    for year in period:
        for state in list_state:
             list_url.append( primary_url.format(  year , state  ) )   


             key_path.append("my_bucket/dados_publicos/TIIS_HOSPITALAR_{}/{}/{}{}.zip".format( date.today() , year , state , year ))
             
    return list_url , period , list_state , key_path ; 



def upload_file_into_s3_bucket(url_path,keys):
    
    s3 = boto3.resource('s3', aws_access_key_id=ACCESS_ID,aws_secret_access_key=ACCESS_KEY) # AWS Secret's should be enviroment variables 
    for url , key  in zip(url_path,keys):
        data = requests.get(url).content
        bucket.upload_fileobj(io.BytesIO(data), Key=key)
        print(  url , key )





if __name__ == '__main__':
    urls,period,states,keys = get_url_list()
    upload_file_into_s3_bucket(  url_path = urls , keys = keys )