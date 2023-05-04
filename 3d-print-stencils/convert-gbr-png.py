#!/usr/bin/python

# Script for conversion gerber files to png image
# output format black and white only


from PIL import Image

def gerberToPNG(filename, png, pixel_mm=0.1):
    """
    Convert to png.
    Return pixel size in mm.
    """
    import numpy as np
    try:
        import gerber
    except Exception as e:
        if 'hull' in str(e).lower():
            raise Exception('Module pyhull not found. Try "pip install pyhull"?')
        raise Exception('The gerber module can be found at https://github.com/curtacircuitos/pcb-tools.')
    print("******* Module 1 load")
    try:
        #from gerber.render import GerberCairoContext
        from gerber.render.cairo_backend import GerberCairoContext
    except Exception as e:
        if 'cairo' in str(e).lower():
            print("TOTO")
            print(str(e))
            print("TOTO")
            raise Exception('Failed to load gerber.render. Do you have the py2cairo package, which provides the cairo module? --->')
        raise e
    print("******  Moduel 2 load")

    # Read gerber and Excellon files
    data = gerber.read(filename)
    data.to_metric()
    
    # Rendering context
    ctx = GerberCairoContext(scale=1.0/pixel_mm) # Scale is pixels/mm

    # Create SVG image
    data.render(ctx)
    ctx.dump(png)
    return png, np.mean(data.size) / np.mean(ctx.size_in_pixels)


#change source and destination base on your needs
destination="destination.png"
gerberToPNG("front-paste.gbr",destination);

img = Image.open(destination)
#add treshold to remove shadows and solve height problems
threshold_value = 128 # adjust threshold value as needed
bw_img = img.convert('L').point(lambda x: 0 if x < threshold_value else 255, mode='1')

bw_img.save(destination)


print("DONE => continue in openscad with: " +str(destination))
