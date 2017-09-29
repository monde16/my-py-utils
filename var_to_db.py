import re


def get_up_indices(s):
    i = -1
    ans = []
    for k in s:
        i+=1
        if k.isupper():
            ans.append(i)
    return ans


def unpretty(s):
    indices = get_up_indices(s)
    fmt = ''
    return fmt


def extract_kt_var(expr):
    var_name = expr.split(':')[0].replace('val ', '').replace('var ', '')
    db_name = unpretty(var_name)


def f(lines):
    return [extract_kt_var(x) for x in lines]


def list_vars(text):
    return text.replace('\n', '').replace(',', '§').split('§')


def main():
    text = '''
    '''
    lines = list_vars(text)
    [print(s) for s in f(lines)]


if __name__ == '__main__':
    main()
