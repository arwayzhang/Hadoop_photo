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
        parts = line.strip().split("\t")

        # Check that the line is of the correct format
        if len(parts) == 7 and parts[5]== '7':  # The line comes from place.txt
            a=parts[6].split("/")
            place_url=""
            for i in a[1:]:
                place_url += i+"/"
            place_id= parts[0].strip()
            print(place_id + "#0\t" + place_url)
        if len(parts) == 7 and parts[5]== '22':
            a=parts[6].split("/")
            place_url=""
            for i in a[1:-1]:
                place_url += i+"/"
            place_id = parts[0].strip()
            print(place_id + "#0\t" + place_url)

        if len(parts) == 6 and '@' in parts[1]:  # The line comes n0*.txt
            place_id, tags = parts[4].strip(), parts[2].strip()
            if tags:
                print(place_id + "#1\t"+tags)
            else:
                print(place_id + "#1\t"+"NULL")

if __name__ == "__main__":
    multi_mapper()
