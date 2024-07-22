import readrides

rows = readrides.read_rides_as_dictionary("Data/ctabus.csv")

# 1 How many bus routes exist in Chicago?
buses = set()
for row in rows:
    buses.add(row["route"])

print(len(buses))

# 2 How many people rode the number 22 bus on February 2, 2011?
# What about any route on any date of your choosing?

peoples = {}
for row in rows:
    peoples[row["date"], row["route"]] = row["rides"]

print(peoples["02/02/2011", "22"])

# What is the total number of rides taken on each bus route?
rides_per_rute = readrides.collections.Counter()
for row in rows:
    rides_per_rute[row["route"]] += row["rides"]

print(rides_per_rute)

# 4 What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?
rides_per_year = readrides.collections.defaultdict(readrides.collections.Counter)
for row in rows:
    tahun = row["date"].split("/")[2]
    rides_per_year[tahun][row["route"]] += row["rides"]

selisih = rides_per_year["2011"] - rides_per_year["2001"]

for key, value in selisih.most_common(5):
    print(key, value)
