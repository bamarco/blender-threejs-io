# Blender Threejs Import and Export
Three.js and Blender are both popular, open source 3d graphics tools. When converting from a scene in Three.js to Blender it is sometimes desirable to specify the camera's properties using the json format.

## Usage
This add-on for Blender is allows for importing Three.js cameras and progrommatically importing Graphics Language Transport Format (glTF) scenes that originated in a Three.js environment. It lays the groundwork for importing other json specified elements, and exporting to json.

- Import supports cameras and glTF scenes.
- Export is not currently supported.

### From the Blender User Interface
``` 
File > Import > Three.js (.json)
```

### From a Blender Python Script
In a blender environment
``` python
import threejs_io
from threejs_io import import_threejs

import_threejs.import_objects("/path/to/threejsConfig.json")
```

### Json Format Specification
The json file consists of a single list of objects that closely resemble Three.js objects with a few extensions. You can see examples in the `examples` folder.

``` json
[{"isScene": true
  "scene": {"filepath": "/path/to/scene.gltf"}
 {"isCamera": true
  "background": {"filepath": "/path/to/reference/backgroundImage.png"}}}]
```

## Installation

### Dependencies
- Install Blender 3.3 or a compatible version
- Install Python 3.10.6 or compatible version
### Archive the threejs_io Folder (.zip)
#### Generic Archival
Zip the `threejs_io` folder using your operating system's zip utility.

#### Linux Archival
```shell
zip -r threejs_io.zip ./threejs_io/
```

### Install from the Blender User Interface 
- `Edit > Preferences > Add-ons > Install`
- Select the `threejs_io.zip` archive

## Development

### Linux

```shell
ln -s ~/path/to/threejs_io/ ~/.config/blender/3.3/scripts/addons/threejs_io
```

Whenever you make changes, restart blender.

## Blender Add-on Template
This project is based on a the `lunadigital` add-on template.

### How to Download the Template
Ready to make your own Blender add-on? Download the latest code, copy it to your project folder, and get started!
    
    git clone https://github.com/lunadigital/blender-addon-template
    cp ./blender-addon-template/* /path/to/your/project/folder
