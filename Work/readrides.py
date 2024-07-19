import collections
import csv
from sys import intern


def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_dictionary(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides
            }
            records.append(record)
    return records

# A class


class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


class RowSlots:
    __slots__ = ['route', 'date', 'daytype', 'rides']

    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def read_rides_as_class(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records


Rowtuple = collections.namedtuple('Row', ['route', 'date', 'daytype', 'rides'])


def read_rides_as_named_tuple(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Rowtuple(route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_class_slots(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = RowSlots(route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_columns(filename):
    ''' 
    Read the bus ride data into 4 lists, representing columns 
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []

    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:

            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes,
                numrides=numrides)

def read_rides_as_columns(filename):
    ''' 
    Read the bus ride data into 4 lists, representing columns 
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []

    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:

            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return 


class RideData(collections.abc.Sequence):
    def __init__(self):
        self.routes = []      # Columns
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        return len(self.routes)

    def __getitem__(self, index):
        # return {'route': self.routes[index],
        #         'date': self.dates[index],
        #         'daytype': self.daytypes[index],
        #         'rides': self.numrides[index]}
        if isinstance(index, int):
            return {
                'route': self.routes[index],
                'date': self.dates[index],
                'daytype': self.daytypes[index],
                'rides': self.numrides[index]
            }
        elif isinstance(index, slice):
            new_ride_data = RideData()
            new_ride_data.routes = self.routes[index]
            new_ride_data.dates = self.dates[index]
            new_ride_data.daytypes = self.daytypes[index]
            new_ride_data.numrides = self.numrides[index]
            return new_ride_data

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])


if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_rides_as_dictionary('Data/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' %
          tracemalloc.get_traced_memory())
