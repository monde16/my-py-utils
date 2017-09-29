import json
import requests


pricing_url = 'http://localhost:8280'


def main():
    cover_request_data = {
        "subscriberName": "Magnum",
        "subscriberPassword": "!Password123",
        "subscriberCode": "100",
        "appId": 28066,
        "appVersion": 1,
        "segment": "DEFAULT",
        "productDescription": "ZAALALK",
        "termType": "WL",
        "escalation": 0,
        "disability": True,
        "gender": "M",
        "bmi": 25,
        "dateOfBirth": "Jan 2, 1976 12:00:00 AM",
        "smoker": "NS",
        "monthlyIncome": 27000,
        "educationLevel": 1,
        "inceptionDate": "Sep 28, 2017 12:00:00 AM",
        "em": 0,
        "pm": 0,
        "lifeDecision": "Standard",
        "occDecision": "Accept",
        "adwDecision": "Accept",
        "commissionSacrifice": 0.02,
        "commissionModel": "M1",
        "premium": 350
    }
    # print(requests.get(pricing_url+'/health'))

    r = requests.post(pricing_url+'/quote/cover', data=cover_request_data)
    print(f'r = {r}')
    print(f'json = {r.json()}')
    print(f'content:\n{r.content}')


if __name__ == '__main__':
    main()
