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

    current_place_url = ""
    current_locality=""
    numphoto = 0

    for key, value in data:
        # Check that the input is valid
        if key == "":
            continue

        #key = key.lower()

        if key != current_place_url:

            if current_place_url != "":
                print(current_locality + "\t" + str(numphoto))

            current_place_url = key
            a=current_place_url.strip().split("/")
            if len(a)>=2:
                current_locality = a[-2]
            else:
                current_locality = "NULL"
            numphoto = int(value)

                #print(current_place_url + "\t" + value)
        else:
            numphoto += int(value)

            
    print(current_locality + "\t" + str(numphoto))
            

        


    
if __name__ == "__main__":
    associate_country()
