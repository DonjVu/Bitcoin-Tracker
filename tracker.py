import requests
import time
api_key = 'a9c337f0-5745-4d7f-83a1-f615cfd2c5af'
bot_token = '1546867954:AAEUV6CRQjyrSs7SMj1SkeQoCl1IsfvsVr0'
chat_id = '1585921327'
threshold = 30000
time_interval = 5 * 60

def get_btc_price():
    url ='https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_key': api_key
    }
    response = requests.get(url, headers=headers)
    response_json = response.json()

    btc_price = response_json['data'][0]
    return btc_price['quote']['USD']['price']

def send_message(chat_id,msg):
    url = f"https://api.telegram.org/bot1546867954:AAEUV6CRQjyrSs7SMj1SkeQoCl1IsfvsVr0/sendMessage?chat_id=1585921327&text={msg}"

    requests.get(url)

def main():
    price_list = []

    while True:
        price = get_btc-price()
        price_list.append(price)

        if price < threshold:
            send_message(chat_id=chatid, msg f'BTC Price Drop Alert: {price}')

        if len(price_list) >= 6:
            send_message(chat_id=chat_id, msg=price_list)
            price_list = []

        time.sleep(time_interval)

main()
