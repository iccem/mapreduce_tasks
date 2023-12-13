#!/usr/bin/env bash

OUT_DIR="result"
NUM_REDUCERS=4

hadoop fs -rm -r -skipTrash $OUT_DIR* > /dev/null

yarn jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -D mapred.job.name="mapred_1" \
    -D mapreduce.job.reduces=${NUM_REDUCERS} \
    -files mapper.py,reducer.py \
    -mapper "python3 ./mapper.py" \
    -combiner "python3 ./reducer.py" \
    -reducer "python3 ./reducer.py" \
    -input /data/wiki/en_articles_part \
    -output $OUT_DIR.tmp > /dev/null

hadoop fs -rm -r -skipTrash ${OUT_DIR} > /dev/null

hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -D mapreduce.job.name="mapred_2" \
    -D mapreduce.job.reduces=1 \
    -files mapper_2.py,reducer_2.py \
    -mapper "python3 ./mapper_2.py" \
    -reducer "python3 ./reducer_2.py" \
    -input ${OUT_DIR}.tmp \
    -output ${OUT_DIR} > /dev/null


hdfs dfs -cat ${OUT_DIR}/part-* | sort -k 2nr |  head -n 50
