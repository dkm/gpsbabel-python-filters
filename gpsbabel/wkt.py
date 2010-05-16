#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   GPSBabel python filters
#   Copyright (C) 20010  Marc Poulhiès
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.


import StringIO

class Track:
    def __init__(self):
        # we are using WGS84, which SRID is 4326 !
        # see http://en.wikipedia.org/wiki/SRID for example

        self.sio = StringIO.StringIO()
        self.sio.write("SRID=4326;")
        self.sio.write("LINESTRING (")
        self.first = True

    def getResult(self):

        return self.sio.getvalue()+")"
    
    def setComputedTrackData(self, distance_meters, 
                             max_alt, min_alt, 
                             max_speed, min_speed,
                             avg_hrt, avg_cad, 
                             start, end, 
                             min_hrt, max_hrt, max_cad):
        pass

    def addPoint(self, lat, lon, 
                 alt, creat, speed, vspeed):
        if not self.first:
            self.sio.write(",")
        else:
            self.first = False
        self.sio.write("%f %f %f" % (lat, lon, alt) )
