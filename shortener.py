from dotenv import load_dotenv
import time
import os
import pyperclip
import requests

load_dotenv()

token = os.environ.get('BITLY_TOKEN')

headers = {'Authorization': f'Bearer {token}'}

groups = requests.get('https://api-ssl.bitly.com/v4/groups', headers=headers)
group_data = groups.json()['groups'][0]
guid = group_data['guid']

url = input('Enter the your long url: ')

shorten_res = requests.post('https://api-ssl.bitly.com/v4/shorten', json={'group_guid': guid, 'long_url': url}, headers=headers)
link = shorten_res.json().get('link')
print('Shortened URL:', link)


while True:
    try: 
        user_res = input('Copy URL to clipboard? (y/n): ')
    except:
        print('Invalid input.')
    else:
        if user_res == 'y':
            pyperclip.copy(link)
            print('URL copied to clipboard.')
            exit()
        elif user_res == 'n':
            exit()
        else:
            print('Invalid input.')
            continue