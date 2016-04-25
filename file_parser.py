# A file contains all the functions required to parse the xml file


def nxt_word(line, cur_position, first_word_sign, last_word_sign):
    """
    :param line: string; a string which contains the next word
    :param cur_position: int; a position from which we should look for a new word
    :param first_word_sign: string; a sign which precedes a new word
    :param last_word_sign: string; a sign which follows a new word
    :return: string; a first word between the signs from the current position in the line
    """
    first_sign_position = line.find(first_word_sign, cur_position)
    last_sign_position = line.find(last_word_sign, first_sign_position + 1)
    if first_sign_position == -1 or last_sign_position == -1:
        return '', 1, 0
    return line[first_sign_position + 1: last_sign_position], 0, last_sign_position + 1


def tags_off(line):
    """
    :param line: string; a string to cut the edge tags signs
    :return: string; a string without edge tag signs
    """
    first_open_tag = line.find('<')
    last_close_tag = line.rfind('>')
    if first_open_tag == -1 or last_close_tag == -1:
        return line
    return line[first_open_tag + 1: last_close_tag]


def line_odd_cut(line, first_sign, last_sign):
    """
    :param line: string; a string to be cut
    :param first_sign: string; a sign before the first emergence of which all the signs will be deleted
    :param last_sign: string; a sign after the last emergence of which all the signs will be deleted
    :return: string; a cut string
    """
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
                 encoding_name="utf-8"):
    """
    :param filename: string; name of the file which content will be returned
    :param content_first_sign: string; a sign that precedes the content; '"' by default
    :param content_last_sign: string; a sign that follows the content; '"' by default
    :param fieldname_first_sign: string; a sign that precedes the field name; ' ' by default
    :param fieldname_last_sign: string; a sign that follows the field name; '=' by default
    :param encoding_name: string; encoding; "utf-8" by default
    :return: list(dict()); parsed content of the file
    """
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
