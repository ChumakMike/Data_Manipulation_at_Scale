import MapReduce
import sys

max_dim = 5
mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    if record[0] == 'a':
        for i in range(max_dim):
            mr.emit_intermediate(str(record[1]) + '' + str(i), record)

    elif record[0] == 'b':
        for i in range(max_dim):
            mr.emit_intermediate(str(i) + '' + str(record[2]), record)

def reducer(key, list_of_values):
    result = 0
    for t1 in list_of_values:
        for t2 in list_of_values:
            if t1[0] == 'a':
                if t1[2] == t2[1] and t2[0] == 'b':
                    tmp = t1[-1] * t2[-1]
                    result += tmp
    mr.emit((int(list(key)[0]), int(list(key)[1]), result))

# Do not modify below this line
# =============================

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)