#!/usr/bin/python3

import sys


def multi_mapper():
    """ This mapper will output different format dependind on input type
    Input format: place_id \t woeid \t latitude \t longitude \t place_name \t place_type_id \t place_url OR
                  photo_id \t owner \t tags \t date_taken \t place_id \t accuracy
    Output format: place_id#0 \t place_url OR
                   place_id#1 \t user \t date
    """
    

    for line in sys.stdin:
        # Clean input and split it
        parts = line.strip().split("=")

        keynum=int(parts[1])
        #keynumstr=str(keynum)

        # Check that the line is of the correct format
        print("{}\t{}".format(parts[0],keynum))

if __name__ == "__main__":
    multi_mapper()
