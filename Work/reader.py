import csv
import logging

logging.basicConfig(level=logging.DEBUG)


def convert_csv(lines, func, *, headers=None):
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    records = []
    for index, row in enumerate(rows, start=1):
        try:
            records.append(func(headers, row))
        except ValueError as e:
            logging.warning(f"Row {index}: Bad Row: {row}")
            logging.debug(f"Row {index}: Reason: {e}")


def csv_as_dicts(lines, types, *, headers=None):
    return convert_csv(
        lines,
        lambda headers, row: {
            name: func(val) for name, func, val in zip(headers, types, row)
        },
        headers=headers,
    )


def csv_as_instances(lines, cls, *, headers=None):
    return convert_csv(lines, lambda headers, row: cls.from_row(row), headers=headers)


def read_csv_as_dicts(filename, types, *, headers=None):
    """
    Read CSV data into a list of dictionaries with optional type conversion
    """
    with open(filename) as file:
        return csv_as_dicts(file, types, headers=headers)


def read_csv_as_instances(filename, cls, *, headers=None):
    """
    Read CSV data into a list of instances
    """
    with open(filename) as file:
        return csv_as_instances(file, cls, headers=headers)
