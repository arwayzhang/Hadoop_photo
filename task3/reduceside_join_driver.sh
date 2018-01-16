#!/bin/bash

if [ $# -lt 3 ]; then
    echo "Invalid number of parameters!"
    echo "Usage: ./job_chain_driver.sh [place_file_location] [input_location] [output_location]"
    exit 1
fi

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
-D stream.num.map.output.key.fields=2 \
-D map.output.key.field.separator=# \
-D mapreduce.partition.keypartitioner.options=-k1,1 \
-D mapreduce.job.maps=1 \
-D mapreduce.job.reduces=5 \
-D mapreduce.job.name='Associate photo with country' \
-file reduceside_join_mapper.py \
-mapper reduceside_join_mapper.py \
-file reduceside_join_reducer.py \
-reducer reduceside_join_reducer.py \
-input $1 \
-input $2 \
-output $3 \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
