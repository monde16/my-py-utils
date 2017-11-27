import re


def get_params(code):
    return re.findall(r'(?<=[(,\s])([\w_][\w_.\d]*|[\w_][\w_.\d]*\(\))(?=[,)])', code)


def get_func(s):
    """
    Returns the method string from s
    :param s: the input string
    :return: the name of a method (if it exists)
    """
    prefix = re.match(r'.+=\s*', s)
    if prefix:
        s = s.replace(prefix.group(), '')
    match = re.match(r'^\s*[\w_]([\w\d_.]?[\w\d_])*\s*(?=\()', s)
    if match:
        return match.group()
    else:
        return ''


def tokenize_method(sig):
    return {'method': get_func(sig), 'params': get_params(sig)}
