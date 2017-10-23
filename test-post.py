import requests


pricing_url = 'http://localhost:8280'
cover_url = f'{pricing_url}/quote/cover'
premium_url = f'{pricing_url}/quote/premium'


def get_cover():
    data = {

    }
    # print(requests.get(pricing_url+'/health'))
    r = requests.post(cover_url, json=data)
    # print(f'r = {r}')
    return r.json()


def get_premium():
    pass


def main():
    print(get_cover())
    data = {

    }
    # print(requests.get(pricing_url+'/health'))
    r = requests.post(pricing_url + '/quote/quote', json=data)
    # print(f'r = {r}')
    return r.json()

if __name__ == '__main__':
    main()
