import csv, io, json

def parse_rows(fmt, data):
    if fmt == 'csv':
        rows = list(csv.DictReader(io.StringIO(data)))
    elif fmt == 'json':
        rows = json.loads(data)
    else:
        raise ValueError('unsupported format')
    if not isinstance(rows, list) or not all(isinstance(r, dict) for r in rows):
        raise ValueError('expected customer object rows')
    return rows
