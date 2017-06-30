import time
import argparse
from PIL import Image

global our_width 
our_width = 58

# This is the main block of code that runs every time someone runs our
# script from the command line.
def main():
    args = parse_args()
    img = load_image(args.image_filename)
    frame = convert_image(img, args.reverse)
    frames = [frame]  # Can change this later to add animations.
    if args.fadein: 
        frames = fadein(img, args.reverse)    
    display_frames(frames)

def fadein(img, reverse):
    # FIXTHIS
    print "Fading in..."
    frames = []
    divisionValue = 250
    for i in range(23):
        print divisionValue
        frame = convert_image(img, reverse, divisionValue) 
        divisionValue -= 10
        frames.append(frame)
    return frames
    

# Load an image from a file, process it, and return to caller.
# Returns the pixels in the format of a single list of integers,
# where each pixel is an integer from [0,255].
def load_image(filename):
    print "Loading image file: " + filename
    new_img = Image.open(filename)
    width, height = new_img.size 
    new_height = our_width
    new_image = new_img.resize((our_width, new_height))
    new_image = new_image.convert("L")
    pixels = list(new_image.getdata())

    return pixels

# Given a pixel, and a reference pixel (both represented as integers
# in the interval [0, 255]), return a pixel value halfway between
# the two pixel values.  Except, the value should not necessarily
# be halfway (0.50), but some percentage of the distance between
# the reference pixel and the given pixel, as specified by refPercentage.
# The value of refPercentage will be a float from the interval [0.0, 1.0].
def mix_pixels(pixel, refPixel, refPercentage=0.0):
    # FIXTHIS
    return 255


# Convert image to ASCII, and return ASCII string to caller.  If the
# 'reverse' variable is set to be true, then use the inverse
# conversion where darks become lights and vice versa. 
def convert_image(pixels, reverse=False, refPixels=None, refPercentage=0.0):
    charlist = ['#','@', '&', '$', '%', 'A', 'X', '+', '!', '<', '*', '^', '"', '=', '~', '-',':', '`', ',' , '.'] 
    divisionValue = 12 
    if reverse:
        print "(Conversion will be done in reverse.)"
        charlist = list(reversed(charlist))

    pixelChars = []
    if refPixels:      # Version one: morphing from a reference image.
        for (pixel, refPixel) in zip(pixels, refPixels):
            mixedPixel = mix_pixels(pixel, refPixel, refPercentage)
            pixelChars.append(charlist[mixedPixel/divisionValue])
    else:              # Version two: normal conversion.
        for pixel in pixels:
            pixelChars.append(charlist[pixel/divisionValue])

    return pixelChars  # A list of characters.

# Given a list of frames represented by ASCII strings, print each
# frame in the list to the screen in order, pausing for 500ms between
# each frame.
def display_frames(frames):
    print "Displaying " + str(len(frames)) + " frames; press [Enter] to start."
    raw_input("")
    for frame in frames:
        display_frame(frame) 
        time.sleep(0.5)

def display_frame(frame):    
    global our_width 
    for i in range(0, len(frame), our_width):
        line = frame[i:i+our_width]
        print ''.join(line)
    
# Helper function for parsing command line arguments. 
def parse_args():
    parser = argparse.ArgumentParser(description='Generate ASCII Art from Images')

    parser.add_argument('image_filename', type=str,
                        help='file containing image')
    parser.add_argument('-r', '--reverse', action='store_true',
                        help='reverse the colors of the image')
    parser.add_argument('-i', '--fadein', action='store_true',
                        help='animate image to fade in from darkness')
    parser.add_argument('-o', '--fadeout', action='store_true',
                        help='animate image to fade out to darkness')
    parser.add_argument('-s', '--scroll', action='store_true',
                        help='animate image to scroll horizontally')
    parser.add_argument('-m', '--morph', nargs=1, type=str,
                        help='animate image morphing into second given image')
    return parser.parse_args()

# Check whether someone is actually running our script from the command line
# (rather than simply importing it as a module.)
if __name__ == "__main__":
    main()
