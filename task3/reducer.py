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
    current_numphoto = 0
    tag_count={}

    for key, value in data:
        # Check that the input is valid
        if key == "":
            continue

        #key = key.lower()

        if key != current_place_url:

            if current_place_url != "":
                sortedtags=sorted(tag_count.items(), key=lambda d:d[1], reverse = True )
                output=""
                k=0

                for tag,freq in sortedtags:
                    
                    k += 1
                    if k <=10:
                        output += "("+tag+":"+str(freq)+")"

                print(str(current_numphoto)+"\t"+current_locality + "\t" + output)
            tag_count={}

            current_place_url = key
            b=value.strip().split("\t")
            
            if len(b)==2:
                current_numphoto = int(b[0])
                current_tags = b[1]
                c=current_tags.strip().split("/")
                for tagandfreq in c:
                    if tagandfreq != "":
                        d=tagandfreq.strip().split(":")
                        if len(d)==2:
                            tag_count[d[0]]=tag_count.get(d[0],0)+int(d[1])
            else:
                current_tags = ""
                current_numphoto = int(value)

            a=current_place_url.strip().split("/")
            if len(a)>=2:
                #a=current_place_url.strip().split("/")
                current_locality = a[-2]
            else:
                current_locality = "NULL"
            
            

                #print(current_place_url + "\t" + value)
        else:
            b=value.strip().split("\t")
            
            if len(b)==2:
                current_numphoto += int(b[0])
                current_tags = b[1]
                c=current_tags.strip().split("/")
                for tagandfreq in c:
                    if tagandfreq != "":
                        d=tagandfreq.strip().split(":")
                        if len(d)==2:
                            tag_count[d[0]]=tag_count.get(d[0],0)+int(d[1])
            else:
                current_tags = ""
                current_numphoto += int(value)



            
    sortedtags=sorted(tag_count.items(), key=lambda d:d[1], reverse = True )
    output=""
    k=0

    for tag,freq in sortedtags:
                    
        k += 1
        if k <=10:
            output += "("+tag+":"+str(freq)+")"

    print(str(current_numphoto)+"\t"+current_locality + "\t" + output)
            

        


    
if __name__ == "__main__":
    associate_country()
