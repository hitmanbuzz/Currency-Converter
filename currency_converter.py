import requests
import json
print('''
Some currencies are:
1. INR (Indian Rupee -> ₹)
2. USD (United States Dollar -> $)
3. GBP (British Pound -> £)

You can also use any other currencies but you need to put the currency format in capital letters eg: inr = INR, usd = USD, etc.

Program Explanation:
1. The first you need to do is type the amount of money.
2. Seconly type the currency you want to exchange. eg: USD to INR which makes it to type USD here.
3. Thirdly type the currency you want to exchange to. eg: USD to INR which makes it to type INR here.
4. Click enter again.
5. You will get a new text file in the same directory where this program was there.
6. The result of the program will be inside the text file.
''')
amount = float(input('Enter the amount of money: '))
currency_from = input('Enter the currency that you want to change: ')
currency_to = input('Enter the currency that you want to change to: ')

url = f'https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}'
payload = {}
headers = {
    'apikey': 'Put the API key here' # You can get the API key from here: https://apilayer.com/marketplace/exchangerates_data-api
}                                    # I am using the free plan for the API key so just like me you can also use the free API Plan to get the key
response = requests.get(url, headers=headers, data=payload)
status_code = response.status_code
result = response.text

# Under this code are specific data are collected
parse_json = json.loads(result)
data_work = parse_json['success']
data_currency_from = parse_json['query']['from']
data_currency_to = parse_json['query']['to']
data_currency_amount = parse_json['query']['amount']
data_convertion_date = parse_json['date']
data_currency_converted_amount = parse_json['result']

print('\n')

# Under this code console print is done
if status_code == 200:
    status_Code = f'Status code: {status_code}'
    status_Work = f'Converting: {data_work}'
    currency_convertion = f'Exchanging/Converting from {data_currency_amount} {data_currency_from} to {data_currency_to} --> {data_currency_converted_amount} {data_currency_to}'
    api_exchange_rate_date = f'The last date when the latest exchange rate was call through the API was: {data_convertion_date}'
    # Python Write files
    with open('result.txt', 'w') as f:
        f.write(f'{status_Code}\n')
        f.write(f'{status_Work}\n')
        f.write(f'{currency_convertion}\n')
        f.write(f'{api_exchange_rate_date}\n')
        f.write('\n')
        f.write('Program made by Hitman-2005(GitHub)')
        f.write('# Thank you for using my currecny exchanger rate with the help of this API!')
        
elif status_code != 200:
    print('''
    Something went wrong because the API Status Code is not 200 which is something wrong related to the API or other stuffs.

    1. If there is any changes in the API which might affect the program, then feel free me to contact me.
    You can check the API Documentation for more about the API!
    Please check the API Documentation here: https://apilayer.com/marketplace/exchangerates_data-api#documentation-tab
    
    2. If there is no any changes in the API which might affect not affect the program.
    Then I will try to check what is wrong with it.
    And I will try to post/upload the new program code file again.
    ''')
else:
    print('Please rerun again and check if any input format such as currencies, etc...')