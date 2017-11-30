from utils import tokenize_method


def enforce_non_null(s):
    s = s.strip()
    tokens = tokenize_method(s)
    return msg(tokens)


def msg(tokens):
    method = tokens['method']
    params = tokens['params']
    return f'''System.out.println("[DEBUG] {method}({', '.join([ f'{p} = "+{p}+"' for p in params ])})");'''


def main():
    s = '''
'''
    for line in [enforce_non_null(line) for line in s.split('\n') if len(line.strip()) > 0]:
        print(line)


if __name__ == '__main__':
    main()
