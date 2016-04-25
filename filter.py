# A function to filter the lists of data according to the rules written in lambdas


def filtered_data(data, field_to_return, filter_fields, filters):
    """
    :param data: list(dict()); data to filter
    :param field_to_return: string; a field which value will be returned if the element passes the filter
    :param filter_fields: list(); a list of fields to be filtered
    :param filters: list(lambda); a list of lambdas to filter the fields
    :return: set(); a set of values from the field 'field to return' of elements which were filtered successfully
    """
    filtered = set()

    if len(filter_fields) != len(filters):
        print('Filter error, lengths of the arrays are not equal')
        return {}

    for i in range(len(data)):
        filter_matching = field_to_return in data[i] # if we have no such a field, I have nothing to return

        for j in range(len(filters)):  # filtering
            if filter_fields[j] not in data[i] or \
               not filters[j](data[i][filter_fields[j]]):
                    filter_matching = False
                    break

        if filter_matching:
            filtered.add(data[i][field_to_return])

    return filtered
