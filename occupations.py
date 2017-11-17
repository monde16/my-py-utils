#!/usr/bin/python3
import csv

csv_occ_max = '/home/phoenix/Downloads/resources/pricing/hiv-pricing/sak-316/csv/Occupation Max Cover.csv'
csv_occ_mappings = '/home/phoenix/Downloads/resources/pricing/hiv-pricing/sak-316/csv/OccupationalConditionEntity.csv'
csv_occ_updated = '/home/phoenix/Downloads/resources/pricing/hiv-pricing/sak-316/csv/OccupationalConditionEntity_output.csv'


# /home/phoenix/wrk/brix_generic_broker/src/main/resources/brix_artifacts/1/seeder/OccupationalConditionEntity.xlsx

def get_rows_dict(filename):
    return csv.DictReader(open(filename, 'r'), delimiter=',', quotechar='"')


def get_rows_list(filename):
    return csv.reader(open(filename, 'r'), delimiter=',', quotechar='"')


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
            d[col] = row[col]
        rows.append(d)
    return rows


def dist_occ(rows, col='Occupation'):
    """
    Create a dictionary of Occupations.
    :param col: the column containing the occupation name
    :param rows: DictReader. Or a dict that contains a column with name coinciding with col parameter
    :return: { Occupation : [ {Product: MaximumCover} ] }. Occupations map, each field has Product:MaximumCover mappings
    """
    occupations = {}
    for row in rows:
        occ = row[col]
        if occ not in occupations:
            occupations[occ] = []
        occupations[occ].append({'Product': row['Product'], 'MaximumCover': row['MaximumCover']})
    return occupations


def constant(values):
    """
    Tests that the values in the given list are the same
    :param values: items to be tested
    :return: True iff all elements in 'values' are the equivalent. Else returns False.
    """
    if len(values) == 0:
        return True
    k = values[0]
    return len([x for x in values if x != k]) == 0


def get_inconsistent(fname):
    """
    :param fname:
    :return: number of product columns with inconsistent cover amounts.
    """
    reader = get_rows_dict(fname)
    occupations = dist_occ(reader)
    inconsistent_occs = []
    for prod_covers in occupations.items():
        (occ, p) = prod_covers
        if not constant([e['MaximumCover'] for e in p]):
            inconsistent_occs.append(occ)
    return inconsistent_occs


def get_distinct_values(fname, col_name):
    """
    Get distinct values in the given column
    :param fname: name of file of csv
    :param col_name: name of the column to process
    :return: a list of distinct values in the specified column
    """
    rows = get_rows_dict(fname)
    s = {row[col_name] for row in rows}
    return [e for e in s]


def is_subset(sub, sup):
    return set(sub) <= set(sup)


def reduce_omc(dlst_omc):
    d = dict()
    for row in dlst_omc:
        d[row['Occupation']] = row['MaximumCover']
    return d


def append_max_covers(dlst_omc, dlst_mappings):
    omc = reduce_omc(dlst_omc)
    for row in dlst_mappings:
        occ = row['Description']
        if occ in omc:
            row['Occupation Maximum Cover'] = omc[occ]
    return dlst_mappings


def add_occ_max_values():
    mappings = dict_reader_to_dict_list(get_rows_dict(csv_occ_mappings), get_header_names(csv_occ_mappings))
    max_covers = dict_reader_to_dict_list(get_rows_dict(csv_occ_max), get_header_names(csv_occ_max))
    return append_max_covers(max_covers, mappings)


def test_occ_names_similar():
    mappings = get_distinct_values(csv_occ_mappings, 'Description')
    max_covers = get_distinct_values(csv_occ_max, 'Occupation')
    return is_subset(max_covers, mappings)


def test_occ_covers_constant():
    return len(get_inconsistent(csv_occ_max)) == 0


def test():
    assert test_occ_covers_constant()
    assert test_occ_names_similar()


def save_csv(data, headers):
    with open(csv_occ_updated, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=headers)

        writer.writeheader()
        for row in data:
            writer.writerow(row)


def main():
    updated = add_occ_max_values()
    if len(updated) == 1: return
    save_csv(updated, updated[0].keys())


if __name__ == '__main__':
    test()
    main()
