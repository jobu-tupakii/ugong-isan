def distribution(text):
    max_seq = ''
    current_seq = ''

    for c in text:
        if c.isdigit():
            current_seq += c
            if len(current_seq) > len(max_seq):
                max_seq = current_seq
        else:
            current_seq = ''


    return max_seq

print(distribution("ab123cd45ef6789gh"))