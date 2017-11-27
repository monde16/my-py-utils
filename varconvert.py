def get_kt_var(s):
    # print(f'get_kt_var >> In: {s}')
    if 'val ' in s:
        s = s.replace('val ', '')
    elif 'var ' in s:
        s = s.replace('var ', '')
    if len(s) == 0:
        return ''
    out = s.split(':')[0]
    # print(f'get_kt_var >> Out: {out}')
    return out


def map_types(type):
    m = {
        'Int': 'INTEGER',
        'Integer': 'INTEGER',
        'int': 'INTEGER',
        'boolean': 'BOOLEAN',
        'Boolean': 'BOOLEAN',
        'long': 'BIGINT',
        'Long': 'BIGINT',
        'String': 'VARCHAR()',
        'Date': 'DATE',
        'BigDecimal': 'NUMERIC',
        'double': '',
        'Double': '',
    }
    return m[type]


def split_on_upper(s):
    # print(f'split_on_upper >> In: {s}')
    if len(s) == 0:
        return []
    indices = []
    for i in range(1, len(s)):
        if s[i].isupper():
            indices.append(i)
    subs = []
    m = 0
    for n in indices:
        subs.append(s[m:n])
        m = n
    subs.append(s[m:])
    # print(f'split_on_upper >> Out: {subs}')
    return subs


def kt2pg(lines):
    # print(f'kt2pg >> In: {lines}')
    word = [get_kt_var(s) for s in lines]
    splits = [split_on_upper(s) for s in word if len(s) > 0]
    # [print(f'\t{s}') for s in splits]
    fmt = ['_'.join(w).lower() + '_' for w in splits]
    # print(f'kt2pg >> Out: {fmt}')
    return fmt


def fmt_vars():
    lines = '''
val premium: BigDecimal
val coverAmount: BigDecimal
'''
    fmt = kt2pg([s.strip() for s in lines.replace(',', '\n').split('\n')])
    [print(s) for s in fmt if len(s) > 0]


def main():
    fmt_vars()


if __name__ == '__main__':
    main()
