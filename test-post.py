import requests


pricing_url = 'http://localhost:8280'
cover_url = f'{pricing_url}/quote/cover'
premium_url = f'{pricing_url}/quote/premium'


def get_cover(appId):
    data = {
        "quoteDate": "2017-10-27T13:19:35+0000",
        "diabetesType": "Type 2",
        "cholStable": 'null',
        "pmOccupational": 0,
        "appVersion": 3,
        "bmi": 23.950617,
        "emMedical": 50,
        "dateOfDiagnosis": "2001-10-31T00:00:00+0000",
        "gender": "M",
        "smokerCigarettesPerDay": 3,
        "subscriberName": "Magnum",
        "pmMedical": 0,
        "cholHigh": False,
        "dateOfBirth": "1962-11-05T00:00:00+0000",
        "bpHigh": False,
        "tempPMMonths": 0,
        "bpConstantDosage": 'null',
        "hba1c": 6.2,
        "neuropathy": False,
        "microAlbuminuria": False,
        "tempPMMedical": 0,
        "smoker": "S",
        "commissionSacrifice": 35,
        "commissionModel": "NIFEP",
        "commissionPercent": 160.000000,
        "alcoholDrinksPerWeek": 2,
        "termInMonths": 276,
        "coverAmount": 75000.000000,
        "inceptionDate": "2017-10-31T05:31:57+0000",
        "partnershipPricing": 10.000000,
        "insulin": True,
        "productCode": "DMUKTERMLIFE",
        "frankProteinuria": False,
        "subscriberPassword": "!Password123",
        "pmPursuits": 0,
        "applicationID": f"{appId}",
        "segment": "DEFAULT",
        "risk": 'null',
        "bpStable": 'null',
        "subscriberCode": "100",
        "cholConstantDosage": 'null',
        "levelOfControl": "Good"
    }
    print(f'Req  #{appId-999}')
    r = requests.post(cover_url, json=data)
    print(f'\tDone #{appId-999}')
    # print(f'r = {r}')
    return r.json()


def get_premium():
    pass


def main():
    for i in range(1000, 2001):
        print(get_cover(i))


if __name__ == '__main__':
    main()
