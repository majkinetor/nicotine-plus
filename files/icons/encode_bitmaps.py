#!/usr/bin/env python3

# COPYRIGHT (C) 2020 Nicotine+ Team
# COPYRIGHT (C) 2016-2017 Michael Labouebe <gfarmerfr@free.fr>
# COPYRIGHT (C) 2009-2010 Quinox <quinox@users.sf.net>
# COPYRIGHT (C) 2006-2009 Daelstorm <daelstorm@gmail.com>
#
# GNU GENERAL PUBLIC LICENSE
#    Version 3, 29 June 2007
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
from os.path import isfile

table = []

for name in sorted(os.listdir(os.path.join("files", "icons", "hilite"))):
    p = os.path.join("files", "icons", "hilite", name)

    if isfile(p):
        table.append([p, name[:-4]])

for name in sorted(os.listdir(os.path.join("files", "icons", "status"))):
    p = os.path.join("files", "icons", "status", name)

    if isfile(p):
        table.append([p, name[:-4]])

flagtable = []

for name in sorted(os.listdir(os.path.join("files", "icons", "flags"))):
    p = os.path.join("files", "icons", "flags", name)

    if isfile(p):
        flagtable.append([p, "flag_%s" % name[:2]])

outf = open(os.path.join("pynicotine", "gtkgui", "imagedata.py"), "w")

for image in sorted(table) + flagtable:
    print(image[0])
    f = open(image[0], "rb")
    outf.write("%s = %r\n" % (image[1], f.read()))
    f.close()

outf.close()
