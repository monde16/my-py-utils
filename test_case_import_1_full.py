import csv

full_test_cases_inf = '/home/phoenix/Downloads/resources/pricing/magnum-pricing/mailed/davej/17-10-24/csv/FullTestCases.csv'
full_test_cases_outf = '/home/phoenix/Downloads/resources/pricing/magnum-pricing/mailed/davej/17-10-24/csv/FullTestCases.txt'

counter = 10

full_test_cases_headers_map = {
    'Commission Model': 'commissionModel',
    'Commission Percentage': 'commissionPercent',
    'Commission Sacrifice': 'commissionSacrifice',
    'Sum Assured': 'coverAmount',
    'DOB': 'dateOfBirth',
    'Date Of Diagnosis': 'dateOfDiagnosis',
    'EM': 'emMedical',
    'Gender': 'gender',
    'HbA1c': 'hba1c',
    'Insulin': 'insulin',
    'PM': 'pmMedical',
    'Smoker': 'smoker',
    'Term': 'termInYears',
    'id': 'applicationID',
    'Premium': 'ExpectedPremium'
}

exclude_set = {
    'Age', 'Years Since Diagnosis', 'LAUTRO', 'Scorecard Loading', 'Policy Fee', 'Base Commission Percetnage'  #, 'Premium'
}


def nexti():
    global counter
    counter = counter + 1
    return counter


default_values = {
    "alcoholDrinksPerWeek": 0,
    "appVersion": 1,
    "applicationID": f"{nexti()}",
    "bmi": 21.860828,
    "bpConstantDosage": 'null',
    "bpHigh": 'false',
    "bpStable": 'null',
    "cholConstantDosage": 'null',
    "cholHigh": 'false',
    "cholStable": 'null',
    "commissionModel": "NIFEP",
    "commissionPercent": 130.00,
    "commissionSacrifice": 0,
    "coverAmount": 150000.000000,
    "dateOfBirth": "1982-08-12",
    "dateOfDiagnosis": "2001-07-30",
    "diabetesType": "Type 2",
    "emMedical": 0,
    "frankProteinuria": 'false',
    "gender": "F",
    "hba1c": 7.8,
    "hba1cAware": 'true',
    "inceptionDate": "2017-10-24",
    "insulin": 'false',
    "lastSmoked": "2017-06-29",
    "levelOfControl": "Good",
    "microAlbuminuria": 'false',
    "neuropathy": 'false',
    "partnershipPricing": 0.00,
    "pmMedical": 0,
    "pmOccupational": 0,
    "pmPursuits": 0,
    "productCode": "DMUKTERMLIFE",
    "quoteDate": "2017-10-24",
    "risk": 'null',
    "segment": "DEFAULT",
    "smoker": "NS",
    "smokerCigarettesPerDay": 23,
    "smokerType": "non-smoker",
    "subscriberCode": "100",
    "subscriberName": "Magnum",
    "subscriberPassword": "!Password123",
    "tempPMMedical": 0,
    "tempPMMonths": 0,
    "termInMonths": 297
}

ints = ['alcoholDrinksPerWeek', 'appVersion', 'smokerCigarettesPerDay', ]
floats = ['bmi', 'commissionPercent', 'commissionSacrifice', 'coverAmount', 'emMedical', 'hba1c', 'partnershipPricing',
          'pmMedical',
          'pmOccupational', 'pmPursuits', 'tempPMMedical', 'tempPMMonths', 'termInMonths']


def add_defaults(rows):
    for row in rows:
        for k in default_values:
            if k not in row:
                row[k] = default_values[k]
    return rows


def map_col(name):
    if name in full_test_cases_headers_map:
        return full_test_cases_headers_map[name]
    else:
        return name


def get_header_names(fname):
    with open(fname) as f:
        reader = csv.reader(f)
        cols = next(reader)
    return cols


def dict_reader_to_dict_list(reader, headers):
    # print(f'Headers: {headers}')
    rows = []
    for row in reader:
        d = dict()
        for col in headers:
            if col not in exclude_set:
                attr_name = map_col(col)
                d[attr_name] = map_val(attr_name, row[col])
        rows.append(d)
    return rows


def update_types(rows):
    for row in rows:
        for k in row:
            if k in ints and isinstance(row[k], str):
                row[k] = int(row[k].replace(',', ''))
            elif k in floats and isinstance(row[k], str):
                row[k] = float(row[k].replace(',', ''))
    return rows


def get_rows_dict(filename):
    reader = csv.DictReader(open(filename, 'r'), delimiter=',', quotechar='"')
    rows = dict_reader_to_dict_list(reader, get_header_names(filename))
    return rows


def map_val(attr, value):
    if attr == 'insulin':
        if value == 'IN':
            return 'true'
        elif value == 'NI':
            return 'false'
        else:
            return value
    elif attr == 'hba1c' or attr == 'commissionSacrifice' or attr == 'commissionPercent' or 'em' in attr or 'pm' in attr:
        return value.replace('%', '')
    else:
        return value


def f(s):
    if len(s) == 0:
        return s
    subs = s.split(' ')
    subs[0] = subs[0].lower()
    for i in range(1, len(subs)):
        subs[i] = subs[i].capitalize()
    return ''.join(subs)


def cleanup(rows):
    for row in rows:
        if 'termInYears' in row:
            row['termInMonths'] = int(row['termInYears']) * 12
            del row['termInYears']
    return rows


def csv_to_json_list(filename):
    rows = get_rows_dict(filename)
    rows = add_defaults(rows)
    rows = cleanup(rows)
    rows = update_types(rows)
    with open(full_test_cases_outf, 'w') as f:
        for row in rows:
            f.write(f'"""{str(row)}""",\n')


def main():
    csv_to_json_list(full_test_cases_inf)


if __name__ == '__main__':
    main()
