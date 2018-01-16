#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Invalid number of parameters!"
    echo "Usage: ./tag_driver.sh [input_location] [output_location]"
    exit 1
fi

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D mapreduce.partition.keycomparator.options=-k1,1nr \
-D mapreduce.job.reduces=1 \
-D mapreduce.job.name='Tag owner inverted list' \
-file mapper.py \
-mapper mapper.py \
-file reducer.py \
-reducer reducer.py \
-input $1 \
-output $2
