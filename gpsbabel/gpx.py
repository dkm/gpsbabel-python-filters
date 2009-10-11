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

import xml.etree.ElementTree as ET # python 2.5
import cStringIO

class Track:

    def acc_normalize(self, acc):
        r = []
        for i in xrange(3):
            zero = self.acc_zero[i]
            one = self.acc_one[i]
            u = one-zero
            v = acc[i]
            
            r.append(float(v-zero)/u)


    def __init__(self, usewii=False):
        self.sio = cStringIO.StringIO()
        self.sio.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>')

        self.gpxroot = ET.Element("gpx", {'xmlns': 'http://www.topografix.com/GPX/1/1',
                                          'creator': '',
                                          'version': '1.1',
                                          'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
                                          'xsi:schemaLocation': 'http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd'})
        self.track = ET.SubElement(gpxroot, "trk")
        ET.SubElement(track, "name").text = "Test GPX"
        self.trkseg = ET.SubElement(track, "trkseg")

        self.wm = None

        if self.usewii :
            import cwiid
            self.wiimote_hwaddr = "00:1D:BC:3B:2D:C3"
            print "You have a few secs to sync with wm..."
            self.wm = cwiid.Wiimote(self.wiimote_hwaddr)
            if self.wm != None:
                print "Ok!"
            else:
                print "Woohoo, we have a problem!"
            self.acc_zero, self.acc_one = self.wm.get_acc_cal(cwiid.EXT_NONE)

            self.rpt_mode = 0
            self.rpt_mode ^= cwiid.RPT_ACC
            self.wm.rpt_mode = self.rpt_mode
            st = self.wm.state
            print "ac data at boot: ", st['acc']

    def getResult(self):
        tree = ET.ElementTree(self.gpxroot)
        tree.write(self.sio)

        return self.sio.getvalue()
    
    def setComputedTrackData(self, distance_meters, 
                             max_alt, min_alt, 
                             max_speed, min_speed,
                             avg_hrt, avg_cad, 
                             start, end, 
                             min_hrt, max_hrt, max_cad):
        pass

    def addPoint(self, lati, longi, 
                 alt, creat, speed, vspeed):

        trkpt = ET.SubElement(self.trkseg, "trkpt", {'lat': lati,
                                                     'lon': longi})
        ET.SubElement(self.tkrpt, "ele").text = alt
        ET.SubElement(self.trkpt, "time").text = creat
        
        if self.wm != None:
            st = self.wm.state
            acc_n = self.acc_normalize(st['acc'])

            ext = ET.SubElement(trkpt, "extensions")
            acc = ET.SubElement(ext, "accelerations", {'x': acc_n[0],
                                                       'y': acc_n[1],
                                                       'z': acc_n[2]})
        
