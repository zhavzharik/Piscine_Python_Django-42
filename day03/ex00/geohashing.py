import sys
import antigravity


def make_geohashing():
    if len(sys.argv) != 4:
        return print("The program takes 3 arguments (latitude, longitude, datedow)!")
    else:
        try:
            lat = float(sys.argv[1])
        except:
            return print("Latitude should be float number!")
        try:
            lon = float(sys.argv[2])
        except:
            return print("Longitude should be float number!")
        try:
            datedow = sys.argv[3].encode('utf-8')
        except:
            return print("Datedow should be string!")
        antigravity.geohash(lat, lon, datedow)


if __name__ == '__main__':
    make_geohashing()
