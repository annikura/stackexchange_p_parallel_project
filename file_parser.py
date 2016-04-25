def nxt_word(line, cur_position, first_word_sign, last_word_sign):
    first_sign_position = line.find(first_word_sign, cur_position)
    last_sign_position = line.find(last_word_sign, first_sign_position + 1)
    if first_sign_position == -1 or last_sign_position == -1:
        return '', 1, 0
    return line[first_sign_position + 1: last_sign_position], 0, \
           last_sign_position + 1


def tags_off(line):
    first_open_tag = line.find('<')
    last_close_tag = line.rfind('>')
    if first_open_tag == -1 or last_close_tag == -1:
        return line
    return line[first_open_tag + 1: last_close_tag]


def line_odd_cut(line, first_sign, last_sign):
    line = tags_off(line)
    first_sign_position = line.find(first_sign)
    last_sign_position = line.rfind(last_sign)
    if first_sign_position == -1 or last_sign_position == -1:
        return ''
    return line[first_sign_position: last_sign_position + 1]


def file_content(filename,
                 content_first_sign='"',
                 content_last_sign='"',
                 fieldname_first_sign=' ',
                 fieldname_last_sign='=',
                 encoding_name='utf-8'):
    data = []
    file = open(filename, 'r', encoding=encoding_name)
    filecontent = file.readlines()
    file.close()
    for s in filecontent:
        line = s
        line = line_odd_cut(line, fieldname_first_sign,
                            content_last_sign)
        if line.find(' Id=') == -1:
            continue
        data.append(dict())
        length = len(data) - 1
        data[length]['__index'] = length
        reading_pointer = 0
        while reading_pointer < len(line):
            fieldname, err, reading_pointer = nxt_word(line, reading_pointer,
                                                       fieldname_first_sign,
                                                       fieldname_last_sign)
            if err:

                break
            content, err, reading_pointer = nxt_word(line, reading_pointer,
                                                     content_first_sign,
                                                     content_last_sign)
            if err:
                break
            data[length][fieldname] = content
    return data
