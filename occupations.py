import csv

csv_occ_max = '/home/phoenix/Downloads/resources/pricing/hiv-pricing/sak-173/occupation_cover_table_V2.csv'
csv_occ_mappings = '/home/phoenix/Downloads/resources/web-app/sak/occupation-mapping.csv'
csv_occ_updated = '/home/phoenix/Downloads/resources/web-app/sak/occupation-mapping2.csv'


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


def dist_occ(rows):
    """
    :param rows: DictReader. Or a dict of Product, Occupation, Cover
    :return: { Occupation : [ {Product: Cover} ] }. Occupations map, each field has Product:cover mappings
    """
    occupations = {}
    for row in rows:
        occ = row['Occupation']
        if occ not in occupations:
            occupations[occ] = []
        occupations[occ].append({'Product': row['Product'], 'Cover': row['Cover']})
    return occupations


def constant(values):
    if len(values) == 0:
        return True
    k = values[0]
    return len([x for x in values if x != k]) == 0


def get_inconsistent(fname):
    reader = get_rows_dict(fname)
    occupations = dist_occ(reader)
    inconsistent_occs = []
    for prod_covers in occupations.items():
        (occ, p) = prod_covers
        if not constant([e['Cover'] for e in p]):
            inconsistent_occs.append(occ)
    return inconsistent_occs


def get_distinct_occ(fname, col_name):
    rows = get_rows_dict(fname)
    s = {row[col_name] for row in rows}
    return [e for e in s]


def is_subset(sub, sup):
    if len(sub) > len(sup): return False
    return len([e for e in sub if e not in sup]) == 0


def reduce_omc(dlst_omc):
    # s = set()
    # for row in dlst_omc:
    #     s.add((row['Occupation'], row['Cover']))
    # return [{'Occupation': t[0], 'Cover': t[1]} for t in s]
    d = dict()
    for row in dlst_omc:
        d[row['Occupation']] = row['Cover']
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
    mappings = get_distinct_occ(csv_occ_mappings, 'Description')
    max_covers = get_distinct_occ(csv_occ_max, 'Occupation')
    return is_subset(max_covers, mappings)


def test_occ_covers_constant():
    return len(get_inconsistent(csv_occ_max)) == 0


def test():
    assert test_occ_covers_constant()
    assert test_occ_names_similar()


def fun(data, headers):
    with open(csv_occ_updated, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=headers)

        writer.writeheader()
        for row in data:
            writer.writerow(row)


def main():
    updated = add_occ_max_values()
    if len(updated) == 1: return
    fun(updated, updated[0].keys())


if __name__ == '__main__':
    test()
    main()
