import requests
import xmltodict
import json

def getfindArriveBusvalue(arsid,busName):
    url = "http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid?serviceKey=NcLi1qt%" \
          "2FoBx9gEdVRGnwMuV%2FleTsOYNyvzXmNBSoHzBxM2dItLH7q0YizLXyPjXCc1peZwxopC0ElwFdn55XjQ%3D%3D&arsId=" + arsid
    response = requests.get(url)
    dict_type = xmltodict.parse(response.text)
    json_type = json.dumps(dict_type)
    result = json.loads(json_type)
    for item in result['ServiceResult']['msgBody']['itemList']:
        if item['rtNm'] == busName :
            print(item)

def getBusArriveTime(arsid):
    url = "http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid?serviceKey=NcLi1qt%" \
          "2FoBx9gEdVRGnwMuV%2FleTsOYNyvzXmNBSoHzBxM2dItLH7q0YizLXyPjXCc1peZwxopC0ElwFdn55XjQ%3D%3D&arsId="+arsid
    response = requests.get(url)
    dict_type = xmltodict.parse(response.text)
    json_type = json.dumps(dict_type)
    result = json.loads(json_type)
    # print(result['ServiceResult']['msgBody']['itemList']['arrmsg1'])
    print(len(result['ServiceResult']['msgBody']['itemList']))

if __name__ == '__main__':
    # getBusArriveTime('03567')
    getfindArriveBusvalue("02005","401")

