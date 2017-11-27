from utils import tokenize_method


def enforce_non_null(s):
    s = s.strip()
    tokens = tokenize_method(s)
    return msg(tokens)


def msg(tokens):
    method = tokens['method']
    params = tokens['params']
    if len(params) == 0 or len(method) == 0:
        return ''
    s = f'if ('
    s += ' || '.join([ f'{p} == null' for p in params])
    s += ') { '
    s += f'''throw new ServiceRuntimeException("Error in {method}: Null value in {{{', '.join([ f'{p} = "+{p}+"' for p in params ])}}}");'''
    s += ' }'
    return s


def main():
    s = '''
calculateMaxCover(BigDecimal coverAmount, BigDecimal productMinCover, BigDecimal productMaxCover, BigDecimal monthlyIncome, BigDecimal occupationMaxCover, StringBuilder accepter) 
'''
    for line in [enforce_non_null(line) for line in s.split('\n') if len(line.strip()) > 0]:
        print(line)


if __name__ == '__main__':
    main()
