#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   GPSBabel python filters
#   Copyright (C) 2009  Marc Poulhiès
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


from igc2kmz import track
from igc2kmz.coord import Coord
from igc2kmz import Flight, flights2kmz

##import pickle
import traceback
import StringIO

from datetime import datetime

class Track:
    def __init__(self):
        self.coords = []

    def getResult(self):
        kwargs = {}
        kwargs['filename'] = "FAKE NAME"

        t = track.Track(self.coords, **kwargs)
 
        f = Flight(t)
        
        try:
            kmz = flights2kmz([f], roots=[], tz_offset=0, task=None)
            sio = StringIO.StringIO()

            kmz.write("TEMP-TEST", '2.2')
        except Exception,e:
            traceback.print_exc()

        return ""
    
    def setComputedTrackData(self, distance_meters, 
                             max_alt, min_alt, 
                             max_speed, min_speed,
                             avg_hrt, avg_cad, 
                             start, end, 
                             min_hrt, max_hrt, max_cad):
        pass

    def addPoint(self, lat, long, 
                 alt, creat, speed, vspeed):
##        print "appending ", lat, long, alt, datetime.fromtimestamp(creat)

        self.coords.append(Coord(lat, long, alt, datetime.fromtimestamp(creat)))
##        print "coords: ", len(self.coords)
