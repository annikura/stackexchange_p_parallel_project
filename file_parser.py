def get_nxt_word(line, cur_position, first_word_sign, last_word_sign):
    first_sign_position = line.find(first_word_sign, cur_position)
    last_sign_position = line.find(last_word_sign, first_sign_position + 1)
    if first_sign_position == -1 or last_sign_position == -1:
        return '', 1, 0
    return line[first_sign_position + 1: last_sign_position], 0, \
           last_sign_position + 1


def cut_the_odd_parts_of_the_line(line, first_sign, last_sign):
    line = line[line.find('<') + 1:]
    first_sign_position = line.find(first_sign)
    last_sign_position = line.rfind(last_sign)
    if first_sign_position == -1 or last_sign_position == -1:
        return ''
    return line[first_sign_position: last_sign_position + 1]


def do_smth_with_that_file(filename,
                           content_first_sign='"',
                           content_last_sign='"',
                           fieldname_first_sign=' ',
                           fieldname_last_sign='=',
                           encoding_name='utf-8'):
    data_structure = []
    file = open(filename, 'r', encoding=encoding_name)
    filecontent = file.readlines()
    file.close()
    for s in filecontent:
        line = s
        line = cut_the_odd_parts_of_the_line(line, fieldname_first_sign,
                                             content_last_sign)
        if line.find(' Id=') == -1:
            continue
        data_structure.append(dict())
        length = len(data_structure) - 1
        data_structure[length]['__index'] = length
        reading_pointer = 0
        while reading_pointer < len(line):
            fieldname, err, reading_pointer = get_nxt_word(line, reading_pointer,
                                                           fieldname_first_sign,
                                                           fieldname_last_sign)
            if err:
                break
            content, err, reading_pointer = get_nxt_word(line, reading_pointer,
                                                         content_first_sign,
                                                         content_last_sign)
            if err:
                break
            data_structure[length][fieldname] = content
    return data_structure
