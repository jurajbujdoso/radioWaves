# Creating PCB stencil on 3D printer

Prove of concept. The Kicat provides vizualizer for pcb gerber files, see bellow. So it should be possible to read this data and create some 3d model.
![alt text](./img/vizual-kicad.png "Title")

 Base on gerber files format it quite chalange to understend it. Multiple dimension array of objects and different format in CNC like format.
 But I found an easy way:

# Starting wiht creation of 3d model


## Install what is required
Install python library:
```
pip install pycairo
pip install pcb-tools
pip install pycairo
pip install numpy
pip install pillow
```

## Convert gerber to picture
I have used what is already there and wrote simplex program which reads gerber files, create image from it. The image will be converted to black and white only.

```
destination="destination.png"
gerberToPNG("front-paste.gbr",destination);

convert-gbr-png.py
```
It will read the file front-paste.gbr and create file destination.png

![alt text](./img/destination.png "Title")

## Postprocessing of picture

Openscad provide way to create 3d model from picture. 
Just open openscad file in same folder, when you have stored result destination.png
```
generate-stl.scad              -- generate just an model, but it will have no holes on the bottom :(
generate-stl-withBottom.scad   -- remove  the bottom problems, suitable for postprocessing
```
![alt text](./img/show-in-openscad.png "")


The example how it looks like with bottom line, this line is unwanted.
![alt text](./img/cut-off.png "with bottom")


After processing in openscad, press F6 and export to stl.
You can process model directly or customize it further in Blender or any other 3d modeling SW.

## Print
Before printing you have to set proper size of the stencil. This can be customized in your printing program.
In my case was the former size 470mm instead of required 47mm.
And I also adjust height to 0.8mm only, probably I would make some testing for optimal heigh.

![alt text](./img/scale-z.png "Title")

