import numpy as np
import datetime
import requests
import os
from datetime import date
from urllib.parse import urlparse
import boto3


def upload_file_into_s3_bucket(url_path):
    s3 = boto3.resource('s3', aws_access_key_id=ACCESS_ID,aws_secret_access_key=ACCESS_KEY) # AWS Secret's should be enviroment variables 
    data = requests.get(url_path).content 
    key = "my_bucket/dados_publicos/TIIS_DADOS_PLANO_{}/dados_plano_saude.csv".format( date.today() ) 
    bucket.upload_fileobj(io.BytesIO(data), Key=key)





if __name__ == '__main__':
    url = "http://ftp.dadosabertos.ans.gov.br/FTP/PDA/TISS/DADOS_DE_PLANOS/DADOS_PLANOS_SAUDE.csv"
    upload_file_into_s3_bucket(  url_path = url  )