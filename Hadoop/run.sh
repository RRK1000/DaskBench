# Requirements
# Hadoop 3.x
# Python 2.7

# WordCount Workload
# dir: DaskBench/Hadoop/Workloads/WordCount
$HADOOP_HOME/bin/hadoop fs -rm -r /wordcount
$HADOOP_HOME/bin/hadoop fs -mkdir /wordcount
$HADOOP_HOME/bin/hadoop fs -put ./Data/WC.txt /wordcount
$HADOOP_HOME/bin/hadoop jar /home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.3.jar -file ./Workloads/WordCount/mapper.py -file ./Workloads/WordCount/reducer.py -mapper ./Workloads/WordCount/mapper.py -reducer ./Workloads/WordCount/reducer.py -input /wordcount/* -output /wordcount/output