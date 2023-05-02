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
import os
import bpy
import bpy.types
import bpy.props
import bpy_extras.io_utils
import warnings

from bpy.types import Operator
from bpy.props import StringProperty, CollectionProperty
from bpy_extras.io_utils import ImportHelper, ExportHelper
from warnings import warn
#class ThreejsConfigProperties(PropertyGroup):
#    path : StringProperty(
#        name = "",
#        description = "Path to three.js configuration json",
#        default = "",
#        maxlen = 1024,
#        subtype = 'FILE_PATH')


class ImportThreejs(Operator, ExportHelper):
    """Import a three.js specified scene"""
    bl_idname = "import_scene.threejs"
    bl_label = "Import Threejs File"

    filename_ext = ".json"

    files: CollectionProperty(
        name = "File Path",
        description = "File path used for importing threejs .json file",
        type = bpy.types.OperatorFileListElement
    )

    directory: StringProperty()

    filter_glob: StringProperty(
        default = "*.json",
        options = {'HIDDEN'},
        maxlen = 255)

    def execute (self, context):
        from threejs_io import import_threejs
        paths = [os.path.join(self.directory, name.name) for name in self.files]

        if not paths:
            paths.append(self.filepath)

        for path in paths:
            import_threejs.import_objects(path, context)

        return {'FINISHED'}

class ExportThreejs(Operator, ImportHelper):
    """Export a three.js specification"""
    bl_idname = "export_scene.threejs"
    bl_label = "Export Threejs File"

    filename_ext = ".json"

    filter_glob: StringProperty(
        default = "*.json",
        options = {'HIDDEN'},
        maxlen = 255)

    def execute (self, context):
        warn("Threejs Export not yet implemented")
        return {'FINISHED'}


# This is where you assign any variables you need in your script. Note that they
# won't always be assigned to the Scene object but it's a good place to start.
def register():
    bpy.utils.register_class(ImportThreejs)
    #bpy.utils.register_class(ExportThreejs)

def unregister():
    bpy.utils.unregister_class(ImportThreejs)
    #bpy.utils.unregister_class(ExportThreejs)
