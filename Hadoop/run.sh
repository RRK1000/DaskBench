# Requirements
# Hadoop 3.x
# Python 2.7

# WordCount Workload
# dir: DaskBench/Hadoop/Workloads/WordCount
read -p "Enter hadoop version: " version
$HADOOP_HOME/bin/hadoop fs -rm -r /wordcount
$HADOOP_HOME/bin/hadoop fs -mkdir /wordcount
$HADOOP_HOME/bin/hadoop fs -put ./Data/WC.txt /wordcount
$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-$version.jar -file ./Workloads/WordCount/mapper.py -file ./Workloads/WordCount/reducer.py -mapper ./Workloads/WordCount/mapper.py -reducer ./Workloads/WordCount/reducer.py -input /wordcount/* -output /wordcount/output
