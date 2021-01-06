import csv
import numpy as np
import pandas as pd
import json
from matplotlib import pyplot as plt

testfile = "/Users/zouyanfeng/PycharmProjects/pythonProject/venv/testfile.txt"
filename = "/Users/zouyanfeng/PycharmProjects/pythonProject/venv/log_zu5_case2.txt"  # Path to log txt file
unsub = "ADASCipvEstimationOP::Set (ID | CIPV | LOC | TTC | dis.x | dis.y )"
perceptionkey = "ADASCipvEstimationOP:: Process end![TimeCost]"
# Unsub contains the keyword of the estimator data



list = []
xlist = []
ylist = []


errorline = 0
fps = []


def main():

    fileimport(filename, unsub, errorline)
    # Start txt file import process, will process text and return an array of coordinates back to main function

    # convertjson()
    # Convert data arrayt to a json file that is compatible with mapping libraries like leaflet

    # plotpoints()
    # Plot x,y points in pylots


def fileimport(filepath, unsub, errorline):
    with open(filepath, 'r') as f:
        lines = csv.reader(f)
        for line in lines:
            errorline = errorline + 1

            if unsub in str(line):
                data = str(line).split(unsub)[1]
                textprocess(data, errorline, line)
                # textprocess function will extract x and y information based on the current log text syntax
            else if 

    f.close()


def textprocess(datastring, errorline, line):
    try:
        datalist = datastring.split("|")
        xvalue = float(datalist[4].strip())
        yvalue = float(datalist[5].strip()[:-2:])

    except:
        print(line)
        print("[error] fpga_can_client.cpp99 [FpgaCanClient] receive message failed")
        return

    xlist.append(xvalue)
    ylist.append(yvalue)

    newarray = [xvalue, yvalue]
    #     # add x,y coordinate to the 3D array
    addarray(newarray)


def addarray(array):
    list.append(array)


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
