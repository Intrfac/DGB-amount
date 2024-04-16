import requests
import urllib.parse
import json

base_url = "https://banking.dgb.co.kr/fst_ebz_20010_1010_t001.jct"

data = {
    "GR_NO":"SECURE",
    "PAYER_NO":"__ID__", # 대구은행 빠른조회용 아이디
    "MHOME_TLNO":"__PW__", # 대구은행 빠른조회용 비밀번호
}

__JSON__ = {
    '_JSON_': urllib.parse.quote_plus(json.dumps(data)).replace('+', '')
}

respond = requests.post(base_url, params=__JSON__)

print(respond.status_code, respond.text)
