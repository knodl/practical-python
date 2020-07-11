# Exercise 3.3
import csv


def parse_csv(filename: str, select: list = None, types: list = None,
              has_headers: bool = True, delimiter: str = ',', silence_errors: bool = False) -> list:
    """
    Parse csv file into a list of records
    :param filename: name of file to read portfolio from
    :param select: list of columns to select from file
    :param types: list of data types for selected columns
    :param has_headers: indicates if there are any headers in file
    :param delimiter: delimiter between columns
    :param silence_errors: indicates if error messages should be shown
    """
    # check edge cases
    if select and silence_errors and not has_headers:
        raise RuntimeError('select argument requires column headers')

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        
        records = []
        # read the file headers
        if has_headers:
            headers = next(rows)
            for n_row, row in enumerate(rows):
                if not row:  # skip rows with no data
                    continue
                record = dict(zip(headers, row))
                filtered_record = record
                if select:
                    headers = select
                    filtered_record = {k: record[k] for k in headers}
                if types:
                    try:
                        filtered_record = {k: func(record[k]) for k, func in zip(headers, types)}
                    except ValueError as e:
                        if not silence_errors:
                            print(f'Row {n_row}: Couldn\'t convert {row}\nRow {n_row}: {e}')
                        continue
                records.append(filtered_record)
            return records
        
        for row in rows:
            if not row:
                continue
            record = [func(val) for func, val in zip(types, row)]
            records.append(tuple(record))
        return records

