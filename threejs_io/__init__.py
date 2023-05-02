# Threejs Import Export Add-on for Blender
# Contributor(s): Brian Marco (brian@mademonkey.com)
#
# Blender Add-on Template
# Contributor(s): Aaron Powell (aaron@lunadigital.tv)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
import bpy

bl_info = {
        "name": "Threejs Import Export (.json)",
        "description": "Import and Export with Threejs",
        "author": "Brian Marco",
        "version": (0, 1),
        "blender": (3, 3, 1),
        "location": "File > Import/Export > Threejs (.json)",
        "warning": "", # used for warning icon and text in add-ons panel
        "wiki_url": "http://my.wiki.url",
        "tracker_url": "http://my.bugtracker.url",
        "support": "COMMUNITY",
        "category": "Import-Export"
        }

def register():
    from threejs_io import properties
    from threejs_io import ui
    properties.register()
    ui.register()

def unregister():
    from threejs_io import properties
    from threejs_io import ui
    properties.unregister()
    ui.unregister()

if __name__ == '__main__':
    register()
