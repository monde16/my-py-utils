from jformat import pretty


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


def scratch3():
    map = {
    }
    for k, v in map.items():
        if isinstance(v, str):
            print(f'Pair("{k}", "{v}"),')
        else:
            print(f'Pair("{k}", {v}),')


def main():
    # scratch()
    # scratch2()
    scratch3()


if __name__ == '__main__':
    main()
