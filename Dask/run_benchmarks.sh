#!/bin/bash
#author: Vishwas
echo "Dask Microbenchmarks"
echo "Press enter when ready"
read n
#mkdir result
#mkdir "exec"
bench_this () {
    echo "$1 benchmark"
    benchname="$1"
    echo $2
    ssh -T darkaether0x1@localhost << HERE
            nohup dask-worker $2 2>/dev/null  1>./dummyout.txt &
            nohup collectl -sZ -i:1 --procfilt fmultiprocessing,cdask-worker -oT > "./result/$benchname"_collectl.txt 2>/dev/null &
HERE
    echo "begin wait"
    sleep 3
    echo "Command execution begins now"
    echo $3
    bash -c "$3"
    sleep 3
    ssh -T darkaether0x1@localhost << 'HERE'
            out=$(ps -ef | grep "collectl -sZ" | head -n 1 | tr -s " " | cut -d ' ' -f2)
            kill -9 $out 
            echo "Killed collectl PID=$out"
            out=$(ps -ef | grep "dask-worker" | head -n 1 | tr -s " " | cut -d ' ' -f2)
            kill -9 $out 
            echo "Killed dask-worker PID=$out"
HERE
    echo "done"
}

echo "Using scheduler $1"
# current_bench="aggregate"
# bench_this $current_bench $1 "{ time python3 aggregate.py 100 10 $1 > ./exec/${current_bench}_exec_out.txt 2>&1 ; } 2>&1 | cat > ./result/${current_bench}_time.txt"

# current_bench="connected_components"
# bench_this $current_bench $1 "{ time python3 connected_components.py 1000 3000 $1 > ./exec/${current_bench}_exec_out.txt 2>&1 ; } 2>&1 | cat > ./result/${current_bench}_time.txt"

# current_bench="filter"
# bench_this $current_bench $1 "{ time python3 filter.py 100 10 $1 > ./exec/${current_bench}_exec_out.txt 2>&1 ; } 2>&1 | cat > ./result/${current_bench}_time.txt"

# current_bench="grep"
# bench_this $current_bench $1 "{ time python3 grep.py 50 $1 > ./exec/${current_bench}_exec_out.txt 2>&1 ; } 2>&1 | cat > ./result/${current_bench}_time.txt"

# current_bench="mat_mult"
# bench_this $current_bench $1 "{ time python3 matmult.py 9000 $1 > ./exec/${current_bench}_exec_out.txt 2>&1 ; } 2>&1 | cat > ./result/${current_bench}_time.txt"

# current_bench="md5_hash"
# bench_this $current_bench $1 "{ time python3 md5_hash.py 20 $1 > ./exec/${current_bench}_exec_out.txt 2>&1 ; } 2>&1 | cat > ./result/${current_bench}_time.txt"

# current_bench="orderby"
# bench_this $current_bench $1 "{ time python3 orderby.py 100 10 $1 > ./exec/${current_bench}_exec_out.txt 2>&1 ; } 2>&1 | cat > ./result/${current_bench}_time.txt"

# current_bench="project"
# bench_this $current_bench $1 "{ time python3 project.py 100 10 $1 > ./exec/${current_bench}_exec_out.txt 2>&1 ; } 2>&1 | cat > ./result/${current_bench}_time.txt"

# current_bench="random_sample"
# bench_this $current_bench $1 "{ time python3 random_sample.py 100 20 $1 > ./exec/${current_bench}_exec_out.txt 2>&1 ; } 2>&1 | cat > ./result/${current_bench}_time.txt"

# current_bench="read"
# bench_this $current_bench $1 "{ time python3 read.py 100 $1 > ./exec/${current_bench}_exec_out.txt 2>&1 ; } 2>&1 | cat > ./result/${current_bench}_time.txt"

# current_bench="scan"
# bench_this $current_bench $1 "{ time python3 scan.py 100 10 $1 > ./exec/${current_bench}_exec_out.txt 2>&1 ; } 2>&1 | cat > ./result/${current_bench}_time.txt"

#current_bench="select"
#bench_this $current_bench $1 "{ time python3 select.py 100 10 $1 > ./exec/${current_bench}_exec_out.txt 2>&1 ; } 2>&1 | cat > ./result/${current_bench}_time.txt"

# current_bench="sort"
# bench_this $current_bench $1 "{ time python3 sort.py 100 $1 > ./exec/${current_bench}_exec_out.txt 2>&1 ; } 2>&1 | cat > ./result/${current_bench}_time.txt"

# current_bench="union"
# bench_this $current_bench $1 "{ time python3 union.py 100 20 100 10 $1 > ./exec/${current_bench}_exec_out.txt 2>&1 ; } 2>&1 | cat > ./result/${current_bench}_time.txt"

current_bench="wordcount"
bench_this $current_bench $1 "{ time python3 wordcount.py 10 $1 0 > ./exec/${current_bench}_exec_out.txt 2>&1 ; } 2>&1 | cat > ./result/${current_bench}_time.txt"

# current_bench="write"
# bench_this $current_bench $1 "{ time python3 write.py 100 $1 > ./exec/${current_bench}_exec_out.txt 2>&1 ; } 2>&1 | cat > ./result/${current_bench}_time.txt"
