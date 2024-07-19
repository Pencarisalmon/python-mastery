import csv


def read_csv_as_dicts(filename, datatypes):
    '''
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append({head: datatype(data)
                           for head, datatype, data in zip(headers, datatypes, row)})

    return records
