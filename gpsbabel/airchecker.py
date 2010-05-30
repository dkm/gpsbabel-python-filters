#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Format converter module using Python.

# Copyright (C) 2010 Marc Poulhiès, dkm@kataplop.net

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111 USA

import os
import os.path
import sys

# TODO:
# - get oair file from cli args
# - use a serialization instead of parsing (check shapefile features)

class Track:
    def __init__(self):
         self.points = []

    def getResult(self):
        return "\n".join(self.points)
    
    def setComputedTrackData(self, distance_meters, 
                             max_alt, min_alt, 
                             max_speed, min_speed,
                             avg_hrt, avg_cad, 
                             start, end, 
                             min_hrt, max_hrt, max_cad):
        pass

    def addPoint(self, lat, lon, 
                 alt, creat, speed, vspeed):
        self.points.append("%f %f %f" %(float(lon), float(lat), float(alt)))

