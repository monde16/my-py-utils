
def sort_strings(s, delim):
    return sorted([st.strip() for st in s.split(delim)])


def main():
    s = '''
'''
    [print(x) for x in sort_strings(s, '\n') if len(x) > 0]


if __name__ == '__main__':
    main()
