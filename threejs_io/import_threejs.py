#!/usr/bin/env python3

# Threejs Import for Blender
# Contributor(s): Brian Marco (brian@mademonkey.com)
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
import json
import math
import mathutils
import warnings

from math import pi, tan, radians
from mathutils import Vector, Euler, Quaternion
from warnings import warn

def with_timing(func):
    import time
    time_start = time.time()
    func()
    print("--Finished in %.4f sec--" % (time.time() - time_start))

def the_default(collection):
    """Get the first item in a collection. If there isn't an item make one."""
    try:
        return collection[0]
    except IndexError:
        return collection.new()

def set_location(obj, position):
    """Converts three.js position to blender location"""
    obj.location.x = position['x']
    obj.location.y = - position['z']
    obj.location.z = position['y']

def axis_to_key(axis):
    return "_" + axis.lower()

def set_rotation(obj, rotation):
    """Converts three.js rotation to blender rotation"""
    rot = obj.rotation_euler

    # have the camera look forward instead of down
    rot.x = pi / 2
    rot.y = 0
    rot.z = 0
    try:
        order = rotation["_order"]
    except KeyError:
        order = "XYZ"

    # performs local/intrinsic rotation rather than global/extrinsic rotation
    axis = order[0]
    rot.rotate_axis(axis, rotation[axis_to_key(axis)])
    axis = order[1]
    rot.rotate_axis(axis, rotation[axis_to_key(axis)])
    axis = order[2]
    rot.rotate_axis(axis, rotation[axis_to_key(axis)])

    if obj.rotation_mode == 'QUATERNION':
        obj.rotation_quaternion = rot.to_quaternion()

def bg_size(camera):
    """Get the size of the camera's background image"""
    try:
        return the_default(camera.data.background_images).image.size
    except AttributeError:
        return None

def bg_aspect(camera):
    """Get the apect ration of the camera's background image"""
    size = bg_size(camera)
    if size:
        aspect = size[0]/size[1]
    else:
        aspect = None
    return aspect

def set_sensor(camera, config):
    """Set all the lens and sensor properties of the camera"""
    gauge = config['filmGauge']
    aspect = config.get('aspect')
    if bg_aspect(camera) and not math.isclose(aspect, bg_aspect(camera)):
        warn("Aspect from camera configuration json and texture image dimensions do not match.\n  config_aspect: %f\n  texture_aspect: %f" \
                 %(aspect, bg_aspect(camera)))
    if not aspect:
        aspect = bg_aspect(camera)
    fov = config['fov']
    offset = config["filmOffset"]
    camera.data.shift_x = offset
    camera.data.sensor_fit = 'AUTO'
    camera.data.sensor_height = gauge / aspect
    camera.data.sensor_width = gauge
    camera.data.lens = (0.5 * gauge / aspect) / tan(radians(fov / 2))

def set_clipping(camera, config):
    """Set the clipping distances of the camera"""
    camera.data.clip_start = config['near']
    camera.data.clip_end = config['far']

def set_background(camera, config):
    """Set the background image of the camera"""
    try:
        image = bpy.data.images.load(config['backgroundImage']['filepath'])
        camera.data.show_background_images = True
        bg = the_default(camera.data.background_images)
        bg.frame_method = 'FIT'
        bg.show_on_foreground = True
        bg.image = image
    except KeyError:
        pass

def set_zoom(camera, config):
    """Warn that camera zoom is not a feature in Blender if zoom is used"""
    try:
        zoom = config["zoom"]
        if zoom != 1:
            warn("Blender does not have a camera.zoom property. Use three.js camera.position or camera.fov to achieve a similar effect.")
    except KeyError:
        pass

def set_depth(camera, config):
    """Set the focus distance and activate focus, if a focus is provided"""
    try:
        focus = config["focus"]
        camera.data.dof.use_dof = True
        camera.data.dof.focus_distance = focus
    except KeyError:
        pass

def set_name(camera, config):
    try:
        camera.name = config['name']
    except KeyError:
        pass

def configure_camera(camera, config):
    """Configure's the camera's settings based on a threejs configuration"""
    # Camera Mode Options
    # camera.data.lens_unit = 'FOV'
    # camera.rotation_mode = 'XYZ'
    camera.data.type = 'PERSP'

    set_name(camera, config)
    set_location(camera, config['position'])
    set_rotation(camera, config['rotation'])
    set_background(camera, config)
    set_sensor(camera, config)
    set_clipping(camera, config)
    set_zoom(camera, config)
    set_depth(camera, config)

def set_output_resolution(scene, camera):
    """Set the output resolution based on the camera's background image"""
    size = bg_size(camera)
    scene.render.resolution_x = size[0]
    scene.render.resolution_y = size[1]

def add_camera(camera_config, context=bpy.context, should_set_resolution=True):
    """Import a threejs camera"""
    cdata = bpy.data.cameras.new(name='Camera')
    camera = bpy.data.objects.new('Camera', cdata)
    context.scene.collection.objects.link(camera)
    configure_camera(camera, camera_config)
    if should_set_resolution:
        set_output_resolution(context.scene, camera)

def add_scene(scene_config, context=bpy.context):
    path = scene_config['scene']['filepath']
    bpy.ops.import_scene.gltf(filepath = path)

def import_objects(filepath, context=bpy.context):
    objects = json.load(open(filepath))
    for obj in objects:
        isCamera = obj.get('isCamera')
        isScene = obj.get('isScene')
        if isCamera:
            add_camera(obj, context)
        elif isScene:
            add_scene(obj, context)
        else:
            warn("Unknown threejs object. Unable to import:\n" + json.dumps(obj))
