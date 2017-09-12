import bluetooth


#this inquire function seems to just find my iPhone
'''
performing inquiry...
found 1 devices
  68:09:27:77:B4:7A - Michael
'''
def inquire():
    print("performing inquiry...")

    nearby_devices = bluetooth.discover_devices(duration=18, lookup_names=True, flush_cache=True)

    print("found %d devices" % len(nearby_devices))

    for addr, name in nearby_devices:
        try:
            print("  %s - %s" % (addr, name))
        except UnicodeEncodeError:
            print("  %s - %s" % (addr, name.encode('utf-8', 'replace')))




def lookup_name(name):  #provide a bluetooth address and it will see if it exists and find the name of the device like Michael
    result = bluetooth.lookup_name(name)
    if result != None:
        print result
        return True
    else:
        return False





if __name__ == "__main__":
    inquire()
    #print lookup_name("B8:27:EB:BA:10:CD")  #pi client address
    #print lookup_name("68:09:27:77:B4:7A")  #iphone address



