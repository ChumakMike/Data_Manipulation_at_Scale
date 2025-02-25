import MapReduce;
import sys;

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      mr.emit_intermediate(w, key)


def reducer(key, list_of_values):
    res = []
    for v in list_of_values:
        if v not in res:
            res.append(v)
    mr.emit((key, res))

# Do not modify below this line
# =============================

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)