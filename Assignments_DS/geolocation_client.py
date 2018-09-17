# Pratyush Singh
# Programming Assignment #11




"""
    This files uses GeoLocation class to create and manipulates three objects for stash, studio and fbi
"""


from geolocation import *

# constructs geolocation object for stash
def stash():
    stash=GeoLocation(34.988889,-106.614444)
    return stash

# constructs geolocation object for studio
def studio():
    studio=GeoLocation(34.989978,-106.614357)
    return studio


# constructs geolocation object for fbi
def fbi():
    fbi=GeoLocation(35.131281,-106.61263)
    return fbi


"""
prints the desired output: latitude and longitude of stash, studio, fbi
it also prints distance in miles between stash/studio  and stash/fbi
"""
def main():
    stash_obj = stash()
    studio_obj = studio()
    fbi_obj = fbi()
    print("the stash is at ", stash_obj.__str__())
    print("ABQ studio is at ", studio_obj.__str__())
    print("FBI building is at", fbi_obj.__str__())
    print("distance in miles between:")
    print("stash/studio = ", stash_obj.distance_from(studio_obj))
    print(" stash/fbi = ", stash_obj.distance_from(fbi_obj))


main()
    


