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


def gen_html(map):
    fmt = []
    for k, v in map.items():
        caption = ' '.join([s.title() for s in split_on_upper(k)])
        fmt.append(f"""<div class="form-group">
    <label for="{k}">{caption}</label>
    <input type="{v}" name="{k}">
</div>""")
    return fmt


def main():
    map = {
    }
    [print(s) for s in gen_html(map)]


if __name__ == '__main__':
    main()
