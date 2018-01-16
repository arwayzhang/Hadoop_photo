#!/usr/bin/python3

import sys


def read_map_output(file):
    """ Return an iterator for key, value pair extracted from file (sys.stdin).
    Input format:  key \t value
    Output format: (key, value)
    """
    for line in file:
        yield line.strip().split("\t",1)


def associate_country():
    """ This reducer perform reduce side join
        Input format: place_id#0 \t place_url OR
                      place_id#1 \t user \t date
        Output format: user \t date \t place_url
        """

    data = read_map_output(sys.stdin)

    current_place_id = ""
    current_place_url = "NULL"
    current_locality ="NULL"
    current_tag=""
    numofphoto=""
    locality={}
    allresult={}
    tag_count = {}
    year=[]

    for i in range(1900,2020):
        year.append(str(i))



    for key, value in data:
        # Check that the input is valid
        if key == "":
            continue

        # Recreate the key by splitting using #
        key = key.split('#')


        # Check if the place_id is the same as before
        if key[0] != current_place_id:

            

            if current_place_id != "":

                sortedtags=sorted(tag_count.items(), key=lambda d:d[1], reverse = True )

                output=current_place_url+"\t"

                k=0

                for tag,freq in sortedtags:
                    
                    k += 1
                    output += "/"+tag+":"+str(freq)

                print(str(count)+"\t"+output.strip())

            count=0
            tag_count = {}    

                #print(current_place_url + "=" + count)

            #print(current_place_url + "=" + count)
            # Check if the key, value pairs come from place.txt (0) or photo (1)
            if key[1] == "0":
                current_place_id = key[0]
                place=value.strip().split("\t")
                current_place_url = place[0]
                #current_place_url = value
                #current_locality =place[1]
                current_place_url_list=current_place_url.lower().split("/")
            else:
                current_place_id = key[0]
                current_place_url = "NULL"
                current_locality ="NULL"
                current_place_url_list=["NULL"]

                #print(current_place_url + "\t" + value)
        elif key[1] == "1":
            if current_place_url != "NULL":
                count += 1

            tags=value.strip().split()
            
            for tag in tags:
                current_tag=tag.lower()
                
                if current_tag not in current_place_url_list and current_tag not in year and current_tag != "NULL":
                    tag_count[current_tag]=tag_count.get(current_tag,0)+1

            
    
    sortedtags=sorted(tag_count.items(), key=lambda d:d[1], reverse = True )

    output=current_place_url+"\t"

    k=0

    for tag,freq in sortedtags:
        
        k += 1
        output += "/"+tag+":"+str(freq)

    print(str(count)+"\t"+output.strip())



    
if __name__ == "__main__":
    associate_country()
