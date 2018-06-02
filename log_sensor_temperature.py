#!/usr/bin/python
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# Can enable debug output by uncommenting:
#import logging
#logging.basicConfig(level=logging.DEBUG)

import time
import os
import Adafruit_MCP9808.MCP9808 as MCP9808
import datetime

# Define a function to convert celsius to fahrenheit.
def c_to_f(c):
	return c * 9.0 / 5.0 + 32.0

sensor = MCP9808.MCP9808()
sensor.begin()

def main():

	while True:
		temp = sensor.readTempC()
		log_temperature( c_to_f(temp) )

		time.sleep(60.0)

def log_temperature(my_temp):
	now = datetime.datetime.now()
	out_temp = str(now) + " - " + str(my_temp)

	my_string_format = "{0:.1f}" 
	me = my_string_format.format(my_temp)
        out_temp = str(now) + " - " + str(me)

	logname = "temperature.log"
	dirpath = os.path.dirname(os.path.realpath(__file__))
	logpath = os.path.join(dirpath,logname)

	f=open(logpath, "a+")
	f.write( out_temp + "\n" )
	f.close()

if __name__== "__main__":
	main()
