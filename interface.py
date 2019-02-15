#!/usr/bin/env python3
import serial
import io
import time
import matplotlib.pyplot as plt

def echelon():
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

    speeds = []

    lastTime = time.time()
    while time.time()-lastTime < 2:
        speed = sio.readline().strip()
        if speed != '':
            lastTime = time.time()
            print(float(speed))
            speeds.append(speed)

    return speeds

if __name__ == '__main__':
    speeds = echelon()
    with open("speeds.txt", "w") as f:
        for speed in speeds:
            f.write(speed)

    t = [i*0.01 for i in range(len(speeds))]
    plt.plot(t, speeds)
    plt.show()
