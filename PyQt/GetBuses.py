import json
import requests
from geopy import geocoders
import sys, traceback
from googleAPIkey import *


response = requests.get("http://dadosabertos.rio.rj.gov.br/apiTransporte/apresentacao/rest/index.cfm/obterTodasPosicoes")
data = response.json()

#Get Address
def latlng_to_addr (lat, lng):
    #key = 'AIzaSyD77KqbrWOwkmSqa6PpXJDsYcvk3fMVt9Y'
    geocoder = geocoders.googlev3.GoogleV3(api_key = key)
    place, point = geocoder.geocode('%s,%s' % (lat, lng))
    return place

#Find specific bus stops
def get_onibus(linha):
    output = ""
    busInfo = ""
    print("entered get_onibus")
    for bus in data['DATA']:
        DATAHORA = bus[0] 
        ORDEM = bus[1] 
        LINHA = bus[2] 
        LATITUDE = bus[3] 
        LONGITUDE = bus[4] 
        VELOCIDADE = bus[5] 
        if bus[2] == linha:
            address = latlng_to_addr(LATITUDE,LONGITUDE)
            #busInfo = "BUS:" + DATAHORA + " " + ORDEM + " " + str(LINHA) + str(VELOCIDADE) + "\nADDRESS:" + address + "\n" + "\n"
            busInfo = "INFO: Hora: %s Ordem: %s Linha: %d Velocidade: %d\n ADDRESS: %s\n\n" % (DATAHORA,ORDEM,LINHA,VELOCIDADE,address)
            print(busInfo)
            output += busInfo
    return output
