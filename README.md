# Blender Threejs Import and Export

## Usage

### User Interface
``` 
File > Import > Three.js (.json)
```

## Dependencies
- Install Blender 3.3 or a compatible version
- Install Python 3.10.6 or compatible version

## Installation

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
