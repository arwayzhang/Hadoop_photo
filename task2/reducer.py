#!/usr/bin/python3

import sys


def read_map_output(file):
    """ Return an iterator for key, value pair extracted from file (sys.stdin).
    Input format:  key \t value
    Output format: (key, value)
    """
    for line in file:
        yield line.strip().split("\t", 1)


def associate_country():
    """ This reducer perform reduce side join
        Input format: place_id#0 \t place_url OR
                      place_id#1 \t user \t date
        Output format: user \t date \t place_url
        """

    data = read_map_output(sys.stdin)

    totalnum=50
    i=0

    current_place_id = ""
    current_place_url = "NULL"
    for key, value in data:
        
        keymod=int(key)
        #keymod=-1*key
        keymodstr=str(keymod)

        

        i += 1

        if i<=50 and value != "NULL":
            print(value+'\t'+keymodstr)
            

        


    
if __name__ == "__main__":
    associate_country()
