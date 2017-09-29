import re


def find_args(line):
    return re.findall(r'(?<=[(,\s])([\w_][\w_.\d]*|[\w_][\w_.\d]*\(\))(?=[,)])', line)


def cat_args(args):
    fmt = ''
    count = 0
    for p in args:
        if count > 0:
            fmt += ', '
        fmt += f'{p}: "+{p}+"'
        count += 1
    return fmt


def fmt_func(s):
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


def pretty(s, initial_big=False):
    if len(s) == 0:
        return ""
    fmtd = ''.join([x for x in s.title().split('_')])
    if initial_big:
        return fmtd
    else:
        if len(fmtd) == 1:
            return fmtd.lower()
        else:
            return fmtd[0].lower() + fmtd[1:]


def fmt_acceptor(assignee):
    lacc = f'{assignee} = '
    racc = f' => "+{assignee}'
    return lacc, racc


def dbg_line(line):
    assert line.count('==') == 0
    parts = [s.strip() for s in line.split('=')]

    if len(parts) == 2:  # has acceptors
        assignee = parts[0]
        expr = parts[1]
        acceptor = assignee
        acceptor = acceptor.split(' ')[-1]  # get the variable name in a declaration
        acceptors = fmt_acceptor(acceptor)
    else:
        return None

    func = fmt_func(expr)

    fmt = cat_args(find_args(line))
    if len(func) > 0:
        return f'System.out.println("[DEBUG] {acceptors[0]}{func}({fmt}){acceptors[1]});'
    elif len(fmt) > 0:
        return f'System.out.println("[DEBUG] {acceptors[0]}{fmt}{acceptors[1]});'


def rem_comments(code):
    """
    Removes single-line comments from code
    :param code: the java source code
    :return: code without single-line comments
    """
    return re.sub(r'\s*//[^\n]*', '', code)


def sys_out(lines):
    lines = rem_comments(lines)
    [print(out) for out in [
        dbg_line(line) for line in lines.split('\n') if len(line) > 0
    ] if out is not None]


def main():
    sys_out('''
BigDecimal minPremium = product.getMinPremium()
maxCover=product.getMaxCover()
baseMargin=product.getBaseMargin()
loadMargin=product.getLoadMargin(),
minGap=product.getMinGap()
maxGap=product.getMaxGap()
policyFee=product.getPolicyFee();
''')


if __name__ == '__main__':
    main()
