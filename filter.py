import sys


def filter_data(data, field_to_return, filter_fields, filters):
    filtered = set()
    if len(filter_fields) != len(filters):
        sys.stderr.wrire('Filter error, lengths of the arrays are not equal')
        return {}
    for i in range(len(data)):
        filter_matching = field_to_return in data[i]
        for j in range(len(filters)):
            if filter_fields[j] not in data[i] or \
               not filters[j](data[i][filter_fields[j]]):
                    filter_matching = False
                    break
        if filter_matching:
            filtered.add(data[i][field_to_return])
    return filtered
