import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)


def reducer(key, list_of_values):
    for orders in list_of_values:
        if orders[0] == 'order':
            for lines in list_of_values:
                if lines[0] == 'line_item':
                    mr.emit(orders + lines)

# Do not modify below this line
# =============================

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
