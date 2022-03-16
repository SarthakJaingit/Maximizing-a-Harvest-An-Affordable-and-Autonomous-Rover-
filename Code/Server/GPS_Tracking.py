import gpsd

def get_location():

    count = 0

    while True:
        count += 1
        try:
            gpsd.connect()
            packet = gpsd.get_current()
            return packet.position()
        except:
            print("{} times pulling gps data".format(count))
            if count > 2000:
                break
            continue





if __name__ == "__main__":

    print(get_location())
