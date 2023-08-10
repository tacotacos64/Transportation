import requests
import json
import pprint

ACCESS_KEY = "ACCESS_KEY"
api_url = "v1/json/station/light"
station_name = "舞鶴"
url = f"https://api.ekispert.jp//{api_url}?key={ACCESS_KEY}&name={station_name}"

res = requests.get(url)
station_json = json.loads(res.text)

for station_data_dict in station_json['ResultSet']['Point']:
    prefecture_name = station_data_dict['Prefecture']['Name']
    station_name = station_data_dict['Station']['Name']
    vehicle_type = station_data_dict['Station']['Type']
    station_code = station_data_dict['Station']['code']
    
    # 辞書型ではなく文字列で返ってくる場合があるため
    if type(vehicle_type) == dict:
        vehicle_type = vehicle_type["text"]
    print(f"県名:{prefecture_name}, 駅名:{station_name}, 乗り物:{vehicle_type}, 駅コード:{station_code}")
# pprint.pprint(station_json['ResultSet']['Point'])
