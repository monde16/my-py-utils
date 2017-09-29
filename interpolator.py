import re


# System.out.println();
# System.out.println("[DEBUG] ");


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
    match = re.match(r'^\s*[\w_][\w\d_.]*\s*(?=\()', s)
    if match:
        return match.group()
    else:
        return ''


def pretty(s, initial_big=False):
    l = s.split('_')
    p = ''
    if initial_big:
        for x in l:
            p += x.capitalize()
    else:
        for i in range(len(l)):
            if i == 0:
                p += l[i].lower()
            else:
                p += l[i].capitalize()
    return p


def scratch():
    methods = ['insulin', 'age_band', 'duration', 'hba1c', 'blood_pressure', 'cholesterol', 'micro_albuminuria',
               'frank_proteinuria', 'neuropathy', 'alcohol', 'smoking']
    fmt = ''
    for m in methods:
        fmt += f"""{pretty(m)} = mapper.map{pretty(m, True)}();\n"""
    print(fmt)


def scratch2():
    vals = ['insulin', 'age_band', 'duration', 'hba1c', 'blood_pressure', 'cholesterol', 'micro_albuminuria',
            'frank_proteinuria', 'neuropathy', 'alcohol', 'smoking']
    for s in vals:
        fmt = pretty(s)
        print(f'System.out.println("{fmt} = "+{fmt});')


def query_scratcher1():
    vals = ['insulin', 'age_band', 'duration', 'hba1c', 'blood_pressure', 'cholesterol', 'micro_albuminuria',
            'frank_proteinuria', 'neuropathy', 'alcohol', 'smoking']
    for s in vals:
        print(f""""AND {s}_ = ? " +""")


def query_scratcher2():
    vals = ['insulin', 'age_band', 'duration', 'hba1c', 'blood_pressure', 'cholesterol', 'micro_albuminuria',
            'frank_proteinuria', 'neuropathy', 'alcohol', 'smoking']
    i = 3
    for s in vals:
        print(f"""ps.setString({i}, {pretty(s)});""")
        i += 1


def dbg_vars():
    args = '''
    '''
    lines_in = [s for s in [s1.strip() for s1 in args.split('\n') if s1 is not None] if len(s) > 0]
    lines_out = []
    for line in lines_in:

        fmt = cat_args(find_args(line))
        func = fmt_func(line)
        if len(func) > 0:
            match_pf = re.match(r'^[\w_][\w_\d]*(?=\s*=\s*)', line)
            acceptor = ''
            lacc = ''
            racc = ''

            if match_pf:
                s = match_pf.group()
                acceptor += f'+" = "+{s}'
                lacc = f'{acceptor} = '
                racc = f'+{acceptor}'

            lines_out.append(f'System.out.println("[DEBUG] {lacc}{func}({fmt})"{racc});')
        elif len(fmt) > 0:
            lines_out.append(f'System.out.println("[DEBUG] {fmt}");')
    return lines_out


def fmt_acceptor(assignee):
    lacc = f'{assignee} = '
    racc = f'+" => "+{assignee}'
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
    return f'System.out.println("[DEBUG] {acceptors[0]}{func}({fmt})"{acceptors[1]});'


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
int x = Integer.parseInt("12");
''')


if __name__ == '__main__':
    main()
