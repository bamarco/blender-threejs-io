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
import bpy.types

from threejs_io.properties import ImportThreejs, ExportThreejs

def menu_import(self, context):
    self.layout.operator(ImportThreejs.bl_idname, text="Three.js (.json)")

def menu_export(self, context):
    self.layout.operator(ExportThreejs.bl_idname, text="Three.js (.json)")

def register():
    bpy.types.TOPBAR_MT_file_import.append(menu_import)
    #bpy.types.TOPBAR_MT_file_export.append(menu_export)

def unregister():
    bpy.types.TOPBAR_MT_file_import.remove(menu_import)
    #bpy.types.TOPBAR_MT_file_export.remove(menu_export)
