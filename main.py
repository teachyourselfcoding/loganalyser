import csv
import numpy as np
import pandas as pd
import json
import re
from matplotlib import pyplot as plt

testfile = "/Users/zouyanfeng/PycharmProjects/pythonProject/loganalyser/logtest.txt"
filename = "/Users/zouyanfeng/PycharmProjects/pythonProject/loganalyser/log_zu5_case2.txt"  # Path to log txt file



#############KEYS
perceptionkey = "ADASCipvEstimationOP:: Process end![TimeCost]"
coordinateskey = "ADASCipvEstimationOP::Set (ID | CIPV | LOC | TTC | dis.x | dis.y )"
framecountkey = "current frame N"

# Unsub contains the keyword of the estimator data



list = []


objectlibrary = {}
#Create dictionary of objects identified


fps = []
linecount = 0

def main():


    fileimport(testfile)
    # Start txt file import process, will process text and return an array of coordinates back to main function

    # convertjson()
    # Convert data arrayt to a json file that is compatible with mapping libraries like leaflet

    # plotpoints()
    # Plot x,y points in pylots

    # for keys, values in objectlibrary.items():
    #     print(keys)
    #     # zipped = "\n".join("{} {}".format(x, y) for x, y in zip(values[0], values[1]))
    #     for t1,t2 in zip(values[0], values[1]):
    #         print('%-20s %s' % (t1, t2))
    #Manual testing: Printing of 3D array


def fileimport(filepath):
    global linecount
    with open(filepath, 'r') as f:
        lines = csv.reader(f)
        for line in lines:
            linecount = linecount + 1
            (textprocess(str(line)))
    f.close()


def textprocess(line):
    if coordinateskey in line:
        extractcoordinates(line)
        # textprocess function will extract x and y information based on the current log text syntax

    if perceptionkey in line:
        extractfps(line)

    if framecountkey in line:
        extractframecount(line)




def extractcoordinates(line):

    data = str(line).split(coordinateskey)[1]
    try:
        datalist = data.split("|")
        objectid = int(datalist[0].strip())
        xvalue = float(datalist[4].strip())
        yvalue = float(datalist[5].strip()[:-2:])

    except:
        print(line)
        print("[error] fpga_can_client.cpp99 [FpgaCanClient] receive message failed")
        return

    # print(objectid, xvalue, yvalue)

    if objectid != 20001:
        print(objectid)
    #Manual test: To check if there is other object ID-ed

    if objectlibrary.get(objectid) == None:

        #New object identified

        xlist = []
        ylist = []
        objectlibrary[objectid] = [xlist, ylist]
        #New array added to array


    objectlibrary[objectid][0].append(xvalue)
    objectlibrary[objectid][1].append(yvalue)
    combinedarray = [xvalue, yvalue]
    #add x,y coordinate to the 3D array


def extractfps(line):
    try:
        data = str(line).split("32mPerception")[1]
        start = "32m"
        end = "ms"
        want = data[data.find(start) + len(start):data.rfind(end)]
        fps = round(1 / float(want)*1000)
    except:
        print(line)
    # print(str(fps) + " fps")


def extractframecount(line):
    frameid = str(line).split(framecountkey)[1].strip()
    # frameid = int(frameid[1:-2])

    # print("frameid" + str(frameid))








def plotpoints():
    # plt.scatter(xlist, ylist)
    plt.plot(xlist, ylist)
    plt.show()



def convertjson():
    df = pd.DataFrame(list, columns=['x', 'y'])
    # Creating a panda dataframe

    # print(df)
    # Printing the panda dataframe

    df.to_json(r'dataframejson.json')
    # Using pandas method to turn this dataframe into json array
    # Will override current file if one already exists!

main()

# def insertarray(xvalue, yvalue):
