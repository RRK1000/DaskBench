from pyspark import SparkConf,SparkContext
import sys


def multiply(row):

    multiply_row = []
    for i in row:
        for j in row:
            multiply = float(i) *float(j)
            multiply_row.append(multiply)
    return multiply_row

def chunks(l, n):
    n = max(1, n)
    return [l[i:i + n] for i in range(0, len(l), n)]

def sum_values(a, b):
    return tuple(sum(x) for x in zip(a,b))

def main():
    conf = SparkConf().setAppName('MatrixMultiply')
    sc = SparkContext(conf=conf)
    assert sc.version >= '1.5.1'

    raw_matrix_file = sc.textFile(sys.argv[1])
    
    matrix = raw_matrix_file.map(lambda line: line.split()).map(lambda value: [float(i) for i in value])


    Col = matrix.take(1)

    nCol = [len(x)for x in Col]
    
    row_permutation = matrix.map(lambda row: multiply(row)).reduce(sum_values)



    matrix_chunks = chunks(row_permutation,nCol[0])


    filelocation = sys.argv[2]

    t_file = open(filelocation,'w')
    i =1
    for num in row_permutation:
        if(i % nCol[0] == 0):
            t_file.write("%s" % num + "\n")

        else:
            t_file.write("%s" % num + " ")
        i = i+1
        


if __name__ == "__main__":
    main()