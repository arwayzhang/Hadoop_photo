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

    current_place_id = ""
    current_place_url = "NULL"
    for key, value in data:
        # Check that the input is valid
        if key == "":
            continue

        # Recreate the key by splitting using #
        key = key.split('#')

        # Check if the place_id is the same as before
        if key[0] != current_place_id:



            if current_place_id != "":
                print(current_place_url + "=" + str(count))

            count=0
            # Check if the key, value pairs come from place.txt (0) or photo (1)
            if key[1] == "0":
                current_place_id = key[0]
                current_place_url = value
            else:
                
                current_place_id = key[0]
                current_place_url = "NULL"    #####?????????????????
                
                #count += 1


                #print(current_place_url + "\t" + value)
        elif key[1] == "1":

            if current_place_url != "NULL":
                count += 1
            
    print(current_place_url + "=" + str(count))


    
if __name__ == "__main__":
    associate_country()
